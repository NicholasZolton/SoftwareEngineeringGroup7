<script lang='ts'>
	import { goto } from "$app/navigation";
	import { user } from "$lib/user";
	
	function logoutUser() {
		user.set(-1);
		goto('/login');
	}
</script>

<div id="navbar" data-theme="light">
	<grad-text><a href="/dashboard">RSVPeats</a></grad-text>	
	{#if $user != -1}
		<a href="/dashboard">My Dashboard</a>
		<a href="/rsvps">My RSVPs</a>
		<a on:click={logoutUser}>Log Out</a>
	{:else}
		<a href="/login">Login</a>
		<a href="/">Sign Up</a>
	{/if}
</div>

<html data-theme="light" lang='en'>
	<slot/>
</html>

<style>
	grad-text a {
		text-decoration: none;
	}

	navbar a {
		text-decoration: none;
	}

	#navbar {
		height: 10vh;
		width: 100%;
		display: flex;
		justify-content: space-around;
		align-items: center;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.25);
		font-size: 1.5rem;
		background: #ffa800;
	}

	grad-text {
		color: #7bbde3;
		background-image: -webkit-linear-gradient(120deg, var(--primary) 0%, #65521b 100%);
		background-clip: text;
		-webkit-background-clip: text;
		text-fill-color: transparent;
		-webkit-text-fill-color: transparent;
		font-weight: 800;
		font-size: 2rem;
	}


	[data-theme="light"],
	:root:not([data-theme="dark"]) {
	--primary: #ff4c04;
	--primary-hover: #e74100;
	--primary-focus: rgba(216, 27, 96, 0.125);
	--primary-inverse: #FFF;
	}
</style>