<script lang='ts'>
	import { onMount } from "svelte";
	import { user } from "$lib/user";
	import { goto } from "$app/navigation";
	let event_id: any = null;
	let foods: any[] | null = null;
	let user_id: number | null = null;
	
	async function getFoods() {
			
		// do the API call to login user, if it returns a token, then set the user	
		const options: any = {method: 'GET', headers: {'User-Agent': 'insomnia/2023.5.8', 'no-cors': true, token: $user.toString()}};

		let response: any = await fetch('http://127.0.0.1:5000/get_foods_for_event?event_id=' + event_id, options)
		// console.log(await response.text());
		response = await response.json();	
		console.log(response);

		foods = response['foods'];
	}
	
	async function getUserInfo() {
			
		// do the API call to login user, if it returns a token, then set the user	
		const options: any = {method: 'GET', headers: {'User-Agent': 'insomnia/2023.5.8', 'no-cors': true, token: $user.toString()}};

		let response: any = await fetch('http://127.0.0.1:5000/get_user_data', options)
		// console.log(await response.text());
		response = await response.json();	
		console.log(response);

		user_id = response['user_data'][0];
	}

	onMount(async () => {
		// get the event_id from the url
		const urlParams = new URLSearchParams(window.location.search);
		event_id = urlParams.get('id');

		await getFoods();
		await getUserInfo();
	});

</script>

<main>
	<h1>Event Foods:</h1>
	{#if foods === null}
		<h1>Loading...</h1>
	{:else if foods.length == 0}
		<h1>There are no foods for this event.</h1>
	{:else}
		{#each foods as food}
			<div id="food">
				<h4>Name: {food[3]}</h4>	
				<h4>Servings: {food[4]}</h4>	
				{#if food[5] == user_id}
					<button on:click={() => {goto('/edit_food?id=' + food[7] + '&event_id=' + event_id)}}>Edit</button>
				{/if}
			</div>
		{/each}
	{/if}
	<button on:click={() => {goto('/create_food?event_id=' + event_id)}}>Add a Food</button>
</main>

<style>

	#food button {
		width: 15%;
		margin: 0;
	}

	#food h4 {
		margin: 0;
	}

	#food {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		width: 100%;
		margin-bottom: 15px;
		
		/* add some drop shadow */
		border-radius: 10px;
		box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.75);
		padding: 10px;
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