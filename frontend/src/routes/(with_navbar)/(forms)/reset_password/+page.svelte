
<script lang='ts'>
	import { goto } from "$app/navigation";
	import { user } from "$lib/user";
	import { onMount } from "svelte";
	let user_info: any = null;
	let email: string = "";
	let oldpassword: string = "";
	let newpassword: string = "";
	let confirmpassword: string = "";
	
	async function getUserInfo() {
			
		// do the API call to login user, if it returns a token, then set the user	
		const options: any = {method: 'GET', headers: {'User-Agent': 'insomnia/2023.5.8', 'no-cors': true, token: $user.toString()}};

		let response: any = await fetch('http://127.0.0.1:5000/get_user_data', options)
		// console.log(await response.text());
		response = await response.json();	
		console.log(response);

		user_info = response['user_data'];
		email = user_info[3];
	}
	
	async function resetPassword() {
		
		if (confirmpassword != newpassword) {
			alert('The passwords do not match. Please try again.');
			oldpassword = "";
			newpassword = "";
			confirmpassword = "";
			return;
		}

		// do the API call to login user, if it returns a token, then set the user	
		let requestBody = {
			"old_password": oldpassword,
			"new_password": newpassword
		};
		const options: any = {
			method: 'POST',
			headers: {'User-Agent': 'insomnia/2023.5.8', 'no-cors': true, token: $user.toString(), 'Content-Type': 'application/json'},
			body: JSON.stringify(requestBody)
		};
		console.log(requestBody)

		let response: any = await fetch('http://127.0.0.1:5000/reset_password', options)
		// console.log(await response.text());
		response = await response.json();
		console.log(response);
		
		if (response['message'] === 'Password updated!') {
			goto('/profile');
		} else {
			alert('There was an error resetting your password. Please try again.');
		}
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
		<h1>Reset Password</h1>

		<div id="input-section">
			<h4>Old Password:</h4>	
			<input type="password" bind:value={oldpassword} placeholder="password123" />
		</div>

		<div id="input-section">
			<h4>New Password:</h4>	
			<input type="password" bind:value={newpassword} placeholder="password123" />
		</div>

		<div id="input-section">
			<h4>Confirm New Password:</h4>	
			<input type="password" bind:value={confirmpassword} placeholder="password123" />
		</div>

		<div id="button-container">
			<button on:click={() => {resetPassword()}}>Save Changes</button>	
		</div>
	{/if}
</main>

<style>

	main {
		width: 100%;
		height: 100%;
	}

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