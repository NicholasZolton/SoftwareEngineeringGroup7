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
  --primary: #d81b60;
  --primary-hover: #c2185b;
  --primary-focus: rgba(216, 27, 96, 0.125);
  --primary-inverse: #FFF;
}

</style>