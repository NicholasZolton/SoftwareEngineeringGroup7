<script lang='ts'>
	import { goto } from "$app/navigation";
	import { user } from "$lib/user";
	import { onMount } from "svelte";
	let food_info: any = null;
	let event_id: any = null;
	let food_name = "";
	let food_servings = "";
	
	async function createFood() {
		// do the API call to login user, if it returns a token, then set the user	
		let requestBody = {
			"event_id": event_id,
			"food_name": food_name,
			"servings": food_servings,
		};
		const options: any = {
			method: 'POST',
			headers: {'User-Agent': 'insomnia/2023.5.8', 'no-cors': true, token: $user.toString(), 'Content-Type': 'application/json'},
			body: JSON.stringify(requestBody)
		};
		console.log(requestBody)
		
		let response: any = await fetch('http://127.0.0.1:5000/add_food', options)	
		// console.log(await response.text());
		response = await response.json();
		console.log(response);

		if (response['message'] === 'Food created!') {
			goto('/view_foods?id=' + event_id);
		} else {
			alert('There was an creating the event. Please try again.');
		}
	}
	
	onMount(async () => {
		const urlParams = new URLSearchParams(window.location.search);
		event_id = urlParams.get('event_id');
	});

</script>

<main>
	<h1>Create a food</h1>

	<div id="input-section">
		<h4>Food Name:</h4>
		<input type="text" bind:value={food_name} placeholder="Turkey" />
	</div>

	<div id="input-section">
		<h4>Servings:</h4>
		<input type="number" bind:value={food_servings} placeholder="5" />
	</div>
	
	<div id="button-container">
		<button on:click={createFood}>Create Food!</button>	
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