<script>
	import successkid from 'images/successkid.jpg';
	import hand from "images/hand.png"
	import store from "images/store.png"
</script>

<style>
	h1 {
		text-align: center;
		margin: 0 auto;
		font-weight: 1000;
		margin: 0 0 0.5em 0;
		width: 40vw;
		font-size: 45px;
	}
	h2 {
		text-align: center;
		margin: 0 auto;
		font-weight: 200;
		margin: 0 0 0.5em 0;
		width: 30vw;
		align-self: center;
		font-size: 28px;
	}

	img {
		width: 100%;
		max-width: 400px;
		margin: 0 0 1em 0;
	}

</style>

<svelte:head>
	<title>SheduleBMSTU</title>
</svelte:head>


<div style="display: flex; flex-direction: row; margin-left: -15%;">
	<div style="margin-top: 50px; display: flex; flex-direction: column">
		<h1>Добро пожаловать</h1>
		<h2>Начните использование SheduleBMSTU уже сейчас</h2>
		<img style="align-self: center; padding-top: 15%" alt="store" width=400px height=70px src="{store}">
	</div>

	<div style="margin-left: 20%; min-width: 550px">
		<img alt="hand" width=550px height=500px src="{hand}">
	</div>
</div>

