<script lang="ts">
	import { goto } from "$app/navigation";
	import { user } from "$lib/user";
	import { onMount } from "svelte";
	import UserIcon from '$lib/icons/UserIcon.svelte';

	let userEvents: any[] | null = null;
	async function getUserEvents() {
		// do the API call to login user, if it returns a token, then set the user	
		const options: any = {method: 'GET', headers: {'User-Agent': 'insomnia/2023.5.8', 'no-cors': true, token: $user.toString()}};

		let response: any = await fetch('http://127.0.0.1:5000/get_my_rsvps', options)
		// console.log(await response.text());
		response = await response.json();	
		console.log(response);
		
		// handle response data
		userEvents = response['events'];
		console.log(JSON.stringify(userEvents));
	}
	
	onMount(async () => {
		console.log($user);
		getUserEvents();	
	});
</script>

<main>
	{#if $user == -1}
		<h1>It appears you aren't logged in.</h1>	
		<h1><a href="/login">Log in now to create and view your RSVPs!</a></h1>	
	{:else if userEvents === null}
		<h1>Loading...</h1>
	{:else if userEvents.length == 0}
		<h1>This is where you can see all your RSVPs.</h1>
		<h1>However, it looks like you don't have any yet.</h1>
	{:else}
		<div id="main-form">
			<div id="user-icon">
				<a href="/profile"><UserIcon css={"width: 30px; height: 30px;"}></UserIcon></a>
			</div>
			<h1>These are all your RSVPs:</h1>
			{#each userEvents as event}
				<div class="event">
					<a href="/view_event?id={event[0]}"><h2>{event[1]}</h2></a>
					<h2>{event[2].substring(0, event[2].length - 3)}</h2>
					<button on:click={() => {goto('/view_event?id=' + event[0])}}>View Event</button>
				</div>
			{/each}
		</div>
	{/if}

</main>

<style>

	#user-icon {
		position: absolute;
		top: 20px;
		left: 20px;
	}

	#main-form {
		position: relative;
		display: flex;
		flex-direction: column;
		justify-content: flex-start;
		align-items: center;
		height: 60%;
		min-height: 60vh;
		width: 80%;
		/* add some drop shadow */
		box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
		border-radius: 10px;
		padding: 20px;
		margin: 5vh;
	}

	main h1 {
		margin-bottom: 10px;
	}

	.event button {
		width: 25%;
		margin: 0;
	}

	.event h2 {
		margin: 0;
	}

	.event {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		height: 10vh;
		width: 75%;
		/* add some drop shadow */
		box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
		border-radius: 10px;
		padding: 20px;
		margin: 1vh;
	}

	main {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		min-height: 90vh;
		width: 100%;
	}	
</style>