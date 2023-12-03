<script lang='ts'>
	import { goto, invalidateAll } from "$app/navigation";
	import { user } from "$lib/user";
	import { onMount } from "svelte";
	let event_info: any = null;
	let event_name = "Friendsgiving";	
	let event_date = "2023-12-05";
	let event_time = "17:30";
	let event_description = "A Thanksgiving for friends!";
	let event_location = "1234 Main St, Dallas, TX 75080";
	let rsvpd: boolean | null = null;
	
	async function rsvpToEvent() {
		// check if the user is logged in
		// if not, redirect to login page with event id
		if ($user === -1) {
			alert('You must be logged in to RSVP to an event.');
			goto('/login?id=' + event_info[0]);
		} else {
			// do the API call to RSVP to the event
			let requestBody = {
				"event_id": event_info[0]
			};
			const options: any = {
				method: 'POST',
				headers: {'Content-Type': 'application/json', 'User-Agent': 'insomnia/2023.5.8', 'no-cors': true, 'token': $user.toString()},
				body: JSON.stringify(requestBody)
			};
			
			let response: any = await fetch('http://127.0.0.1:5000/rsvp_to_event', options)
			// console.log(await response.text());
			response = await response.json();
			console.log(response);
			
			if (response['message'] === 'RSVP created!') {
				rsvpd = true;
			} else {
				alert('There was an error RSVPing to the event. Please try again.');
			}
		}
	}

	async function unrsvpToEvent() {
		// check if the user is logged in
		// if not, redirect to login page with event id
		if ($user === -1) {
			alert('You must be logged in to RSVP to an event.');
			goto('/login?id=' + event_info[0]);
		} else {
			// do the API call to RSVP to the event
			let requestBody = {
				"event_id": event_info[0]
			};
			const options: any = {
				method: 'POST',
				headers: {'Content-Type': 'application/json', 'User-Agent': 'insomnia/2023.5.8', 'no-cors': true, 'token': $user.toString()},
				body: JSON.stringify(requestBody)
			};
			
			let response: any = await fetch('http://127.0.0.1:5000/unrsvp_to_event', options)
			// console.log(await response.text());
			response = await response.json();
			console.log(response);
			
			if (response['message'] === 'RSVP deleted!') {
				rsvpd = false;
			} else {
				alert('There was an error deleting your RSVP. Please try again.');
			}
		}
	}

	async function getEventInfo() {
		// get the event_id from the url
		const urlParams = new URLSearchParams(window.location.search);
		const event_id = urlParams.get('id');

		// do the API call to get event info			
		const options: any = {method: 'GET', headers: {'User-Agent': 'insomnia/2023.5.8', 'no-cors': true}};

		let response: any = await fetch('http://127.0.0.1:5000/get_event?event_id=' + event_id, options)
		// console.log(await response.text());
		response = await response.json();	
		console.log(response);
		
		// handle response data
		event_info = response['event'];
		console.log(JSON.stringify(event_info));
		
		// set the event info
		event_name = event_info[1];
		event_date = event_info[2].split(' ')[0];
		event_time = event_info[2].split(' ')[1].substring(0, 5);
		event_description = event_info[3];
		event_location = event_info[4];
	}
	
	async function getReservationInfo() {
		// get the event_id from the url
		const urlParams = new URLSearchParams(window.location.search);
		const event_id = urlParams.get('id');

		// do the API call to get event info			
		const options: any = {method: 'GET', headers: {'User-Agent': 'insomnia/2023.5.8', 'no-cors': true, 'token': $user.toString()}};
		
		let response: any = await fetch('http://127.0.0.1:5000/check_if_rsvpd?id=' + event_id, options);
		// console.log(await response.text());
		response = await response.json();
		console.log(response);
		
		if (response['message'] === 'User not logged in') {
			rsvpd = false;
			return;
		}

		rsvpd = response['rsvpd']
	}

	onMount(async () => {
		// get the event info
		await getEventInfo();
		await getReservationInfo();
		console.log('current user: ' + $user);
	});

</script>


<main>

	<div id="event-box">
		{#if event_info !== null}
		<div id="event-view">
			<div id="event-title">
				<h1>{event_name}</h1>
				<img src="https://risanb.com/code/colorful-google-maps-marker/default-marker.jpg" />
			</div>
			<div id="event-grid">
				<div id="left-column">
					<h3>Description:</h3>
					<h4>{event_description}</h4>
					<h3>Date:</h3>	
					<h4>{event_date}</h4>
				</div>
				<div id="right-column">
					<h3>Location:</h3>
					<h4>{event_location}</h4>
					<h3>Time:</h3>	
					<h4>{event_time}</h4>
				</div>
			</div>
			{#if rsvpd == false}
				<button on:click={() => rsvpToEvent()}>RSVP</button>
			{:else if rsvpd == null}
				<button disabled>Checking RSVP...</button>
			{:else}
				<button on:click={() => unrsvpToEvent()}>Un-RSVP</button>
			{/if}

			{#if rsvpd == true}
				<button id="food-button" on:click={() => {goto('/view_foods?id=' + event_info[0])}}>View Foods</button>
			{:else}
				<button disabled>RSVP to view foods</button>
			{/if}
		</div>	
		{:else}
		<div id="centerer">
			<h1>Loading...</h1>
		</div>
		{/if}
	</div>

</main>


<style>

	#centerer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		width: 100%;
		height: 100%;
	}

	#event-view button {
		margin: 0;
		margin-top: 10px;
	}

	#event-title img {
		width: 30%;
	}

	#event-title {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: space-around;
	}

	#right-column h3 {
		margin-bottom: 0px;
	}

	#left-column h3 {
		margin-bottom: 0px;
	}

	#left-column {
		grid-column: 1 / span 6;
		grid-row: 1 / span 12;
	}
	
	#right-column {
		grid-column: 7 / span 6;
		grid-row: 1 / span 12;
	}

	#event-grid {
		display: grid;
		grid-template-columns: repeat(12, 1fr);
		grid-template-rows: repeat(12, 1fr);
	}

	#event-view {
		display: flex;
		flex-direction: column;
		justify-content: center;
	}

	#event-box {
		grid-column: 2 / span 10;
		grid-row: 2 / span 10;
		background-color: #fff;
		border-radius: 10px;
		box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
		padding: 40px;
	}

	main {
		display: grid;
		min-height: 90vh;
		grid-template-columns: repeat(12, 1fr);
		grid-template-rows: repeat(12, 1fr);
	}

</style>