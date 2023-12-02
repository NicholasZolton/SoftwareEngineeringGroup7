
<script lang='ts'>
	import { goto } from "$app/navigation";
	import { user } from "$lib/user";
	import { onMount } from "svelte";
	let user_info: any = null;
	
	async function getUserInfo() {
			
		// do the API call to login user, if it returns a token, then set the user	
		const options: any = {method: 'GET', headers: {'User-Agent': 'insomnia/2023.5.8', 'no-cors': true, token: $user.toString()}};

		let response: any = await fetch('http://127.0.0.1:5000/get_user_data', options)
		// console.log(await response.text());
		response = await response.json();	
		console.log(response);

		user_info = response['user_data'];
	}
	
	onMount(async () => {
		console.log($user);
		await getUserInfo();
	});

</script>

<main>
	{#if user_info === null}
		<h1>Loading...</h1>
	{:else}
		<h1>Welcome, {user_info[1]}!</h1>

		<div id="input-section">
			<h4>Username:</h4>	
			<h4>{user_info[1]}</h4>
		</div>

		<div id="input-section">
			<h4>Email:</h4>	
			<h5>{user_info[3]}</h5>
		</div>

		<div id="input-section">
			<h4>Password:</h4>	
			<h5>********</h5>
		</div>

		<div id="button-container">
			<button on:click={() => {goto('/reset_password')}}>Reset Password</button>	
		</div>
	{/if}
</main>

<style>
	#input-section h4 {
		margin: 0;
	}

	#input-section h5 {
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
		margin: 20px 0;
	}
</style>