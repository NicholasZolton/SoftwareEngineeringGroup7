<script lang='ts'>
	import { user } from "$lib/user";
	import { goto } from "$app/navigation";
	import { onMount } from "svelte";
	let email = "adalovelace@example.com";
	let password = "adalovelace";
	let id: string | null = null;

	async function loginUser(event: any) {
		event.preventDefault();
		// do the API call to login user, if it returns a token, then set the user	
		let requestBody = {
			"email": email,
			"password": password
		};
		const options: any = {
			method: 'POST',
			headers: {'Content-Type': 'application/json', 'User-Agent': 'insomnia/2023.5.8', 'no-cors': true},
			body: JSON.stringify(requestBody)
		};

		let response: any = await fetch('http://127.0.0.1:5000/login_user', options)
		// console.log(await response.text());
		response = await response.json();
		console.log(response);
		
		if (response['message'] === 'User found') {
			user.set(response['token'])
			if (id != null) {
				goto('/view_event?id=' + id);
			} else {
				goto('/dashboard');
			}
		} else {
			alert('There was an error logging in. Please try again.');
		}
	}
	
	onMount(async () => {
		console.log('current user: ' + $user);
		
		// try to find an id from the URL
		const urlParams = new URLSearchParams(window.location.search);
		id = urlParams.get('id');
		console.log('id: ' + id);
	});

</script>


<main>
	<!-- This is the is login page. -->
	<div id="form">
		<h1>Login</h1>
		
		<div id="input-section">
			<h4>Email:</h4>
			<input type="text" bind:value={email} placeholder="test@example.com" />
		</div>

		<div id="input-section">
			<h4>Password:</h4>
			<input type="password" bind:value={password} placeholder="password123" />
		</div>
		
		<div id="button-container">
			<button on:click={loginUser}>Login!</button>	
		</div>

	</div>
</main>


<style>

	#input-section h4 {
		margin: 0;
	}

	#form h1 {
		margin: 0;
	}

	#input-section {
		width: 100%;
		display: flex;
		flex-direction: column;
		justify-content: flex-start;
		align-items: flex-start;
	}

	#form {
		display: flex;
		flex-direction: column;
		justify-content: flex-start;
		align-items: center;
		height: 60%;
		min-height: 60vh;
		width: 40%;
		/* add some drop shadow */
		box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
		border-radius: 10px;
		padding: 20px;
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