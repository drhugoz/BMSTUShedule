<script>
	import Nav from '../components/Nav.svelte';
	import Footer from "../components/Footer.svelte";
	
	export let segment;
</script>

<style>
	main {
		position: relative;
		max-width: 56em;
		min-height: 100vh;
		background-color: #f1e4d4;
		padding: 2em;
		margin: 0 auto;
		box-sizing: border-box;
	}
	.superclass {
		font-family: Comfortaa;
		background-color: #f1e4d4;
	}
</style>


<div class="superclass">
<Nav {segment}/>

<main>
	<slot></slot>
</main>

<Footer {segment}/>

</div>