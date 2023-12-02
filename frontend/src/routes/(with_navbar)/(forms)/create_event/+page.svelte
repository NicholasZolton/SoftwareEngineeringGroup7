<script lang='ts'>
	import { goto } from "$app/navigation";
	import { user } from "$lib/user";

	let event_name = "Friendsgiving";	
	let event_date = "2023-12-05";
	let event_time = "17:30";
	let event_description = "A Thanksgiving for friends!";
	let event_location = "1234 Main St, Dallas, TX 75080";

	async function createEvent(event: any) {
		event.preventDefault();
		// do the API call to login user, if it returns a token, then set the user	
		let requestBody = {
			"event_name": event_name,
			"event_date": event_date,
			"event_time": event_time,
			"event_description": event_description,
			"event_location": event_location
		};
		const options: any = {
			method: 'POST',
			headers: {'User-Agent': 'insomnia/2023.5.8', 'no-cors': true, token: $user.toString(), 'Content-Type': 'application/json'},
			body: JSON.stringify(requestBody)
		};
		console.log(requestBody)

		let response: any = await fetch('http://127.0.0.1:5000/create_event', options)
		// console.log(await response.text());
		response = await response.json();
		console.log(response);
		
		if (response['message'] === 'Event created!') {
			goto('/dashboard');
		} else {
			alert('There was an creating the event. Please try again.');
		}
	}

</script>

<main>
	<h1>Create a new event</h1>

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
		<button on:click={createEvent}>Create Event!</button>	
	</div>
</main>

<style>
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
</style>