<script lang='ts'>
</script>

<svelte:head>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">	
</svelte:head>

<html data-theme="light" lang='en'>
	<slot/>
</html>

<style>
[data-theme="light"],
:root:not([data-theme="dark"]) {
	--primary: #ff4c04;
	--primary-hover: #e74100;
	--primary-focus: rgba(216, 27, 96, 0.125);
	--primary-inverse: #FFF;
}

</style>