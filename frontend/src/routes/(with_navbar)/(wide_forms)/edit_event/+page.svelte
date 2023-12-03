<script lang='ts'>
	import { goto } from "$app/navigation";
	import { user } from "$lib/user";
	import { onMount } from "svelte";
	let event_info: any = null;
	let event_name = "Friendsgiving";	
	let event_date = "2023-12-05";
	let event_time = "17:30";
	let event_description = "A Thanksgiving for friends!";
	let event_location = "1234 Main St, Dallas, TX 75080";
	
	async function deleteEvent() {
		// get the event_id from the url
		const urlParams = new URLSearchParams(window.location.search);
		const event_id = urlParams.get('id');

		// do the API call to login user, if it returns a token, then set the user	
		let requestBody = {
			"event_id": event_id,
		};
		const options: any = {
			method: 'POST',
			headers: {'User-Agent': 'insomnia/2023.5.8', 'no-cors': true, token: $user.toString(), 'Content-Type': 'application/json'},
			body: JSON.stringify(requestBody)
		};
		console.log(requestBody)
		
		let response: any = await fetch('http://127.0.0.1:5000/delete_event', options)	
		// console.log(await response.text());
		response = await response.json();
		console.log(response);

		if (response['message'] === 'Event deleted!') {
			goto('/dashboard');
		} else {
			alert('There was an error deleting the event. Please try again.');
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
		event_time = event_info[2].split(' ')[1];
		event_description = event_info[3];
		event_location = event_info[4];
	}
	
	async function editEvent(event: any) {
		event.preventDefault();
		// do the API call to login user, if it returns a token, then set the user	
		let requestBody = {
			"event_id": event_info[0],
			"event_name": event_name,
			"event_date": event_date,
			"event_time": event_time.substring(0, 5),
			"event_description": event_description,
			"event_location": event_location
		};
		const options: any = {
			method: 'POST',
			headers: {'User-Agent': 'insomnia/2023.5.8', 'no-cors': true, token: $user.toString(), 'Content-Type': 'application/json'},
			body: JSON.stringify(requestBody)
		};
		console.log(requestBody)

		let response: any = await fetch('http://127.0.0.1:5000/edit_event', options)
		// console.log(await response.text());
		response = await response.json();
		console.log(response);
		
		if (response['message'] === 'Event updated!') {
			goto('/dashboard');
		} else {
			alert('There was an creating the event. Please try again.');
		}
	}

	onMount(async () => {
		await getEventInfo();
	});

</script>

<main>
	{#if event_info === null}
		<h1>Loading...</h1>
	{:else}
		<h1>Edit this event</h1>

		<div id="input-section">
			<h4>Event Name:</h4>
			<input type="text" bind:value={event_name} placeholder="Friendsgiving" />
		</div>

		<div id="input-section">
			<h4>Event Date:</h4>
			<input type="date" bind:value={event_date} placeholder="2023-12-05" />
		</div>

		<div id="input-section">
			<h4>Event Time:</h4>
			<input type="time" bind:value={event_time} placeholder="17:30" />
		</div>

		<div id="input-section">
			<h4>Event Description:</h4>
			<input type="text" bind:value={event_description} placeholder="A Thanksgiving for friends!" />
		</div>
		
		<div id="input-section">
			<h4>Event Location:</h4>
			<input type="text" bind:value={event_location} placeholder="1234 Main St, Dallas, TX 75080" />
		</div>

		<div id="button-container">
			<button on:click={editEvent}>Update Event!</button>	
			<button on:click={deleteEvent}>Delete Event!</button>	
		</div>
	{/if}
</main>

<style>
	#button-container button {
		width: 15%;
	}

	#button-container {
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		align-items: center;
		width: 100%;
	}

	#input-section h4 {
		margin: 0;
	}

	h1 {
		margin-bottom: 10px;
	}

	#input-section {
		width: 100%;
		display: flex;
		flex-direction: column;
		justify-content: flex-start;
		align-items: flex-start;
	}
	
	main {
		display: flex;
		flex-direction: column;
		justify-content: flex-start;
		align-items: center;
		height: 100%;
		width: 100%;
	}
</style>