<script lang='ts'>
	import { goto } from "$app/navigation";
	import { user } from "$lib/user";
	import { onMount } from "svelte";
	let food_info: any = null;
	let event_id: any = null;
	let food_name = "";
	let food_servings = "";
	
	async function getFood() {
		// get the event_id from the url
		console.log(window.location.toString());
		const urlParams = new URLSearchParams(window.location.search);
		const food_id = urlParams.get('id');
		event_id = urlParams.get('event_id');

		// do the API call to get event info
		const options: any = {method: 'GET', headers: {'User-Agent': 'insomnia/2023.5.8', 'no-cors': true}};

		let response: any = await fetch('http://127.0.0.1:5000/get_food?food_id=' + food_id, options)
		// console.log(await response.text());
		response = await response.json();
		console.log(response);

		// handle response data
		food_name = response['food'][4];
		food_servings = response['food'][5];
		food_info = response['food'];
	}

	async function editFood(event: any) {
		event.preventDefault();
		// do the API call to login user, if it returns a token, then set the user	
		let requestBody = {
			"food_id": food_info[0],
			"food_name": food_name,
			"servings": food_servings
		};
		const options: any = {
			method: 'POST',
			headers: {'User-Agent': 'insomnia/2023.5.8', 'no-cors': true, token: $user.toString(), 'Content-Type': 'application/json'},
			body: JSON.stringify(requestBody)
		};
		console.log(requestBody)

		let response: any = await fetch('http://127.0.0.1:5000/edit_food', options)
		// console.log(await response.text());
		response = await response.json();
		console.log(response);
		
		if (response['message'] === 'Food updated!') {
			goto('/view_foods?id=' + event_id);
		} else {
			alert('There was an creating the event. Please try again.');
		}
	}
	
	onMount(async () => {
		await getFood();
	});

</script>

<main>
	<h1>Edit this food</h1>

	{#if food_info === null}
		<h1>Loading...</h1>
	{:else}
		<div id="input-section">
			<h4>Food Name:</h4>
			<input type="text" bind:value={food_name} placeholder="Turkey" />
		</div>

		<div id="input-section">
			<h4>Servings:</h4>
			<input type="number" bind:value={food_servings} placeholder="5" />
		</div>
		
		<div id="button-container">
			<button on:click={editFood}>Save Changes!</button>	
		</div>
	{/if}
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