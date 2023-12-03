<script lang='ts'>
	import { goto } from "$app/navigation";
	import { user } from "$lib/user";
	import { onMount } from "svelte";
</script>

<main>
	{#if $user == -1}
		<h1>You are not logged in.</h1>
		<h1>Please <a href="/login">login</a> to access this page.</h1>
	{:else}
		<div id="form">
			<slot/>
		</div>
	{/if}
</main>

<style>
	#form {
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

	main {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		min-height: 90vh;
		width: 100%;
	}
</style>