<script>
	let answer;
	let specInp = "Терапия";
	let nameInp = "Водзинская Татьяна Владимировна";
  let baseUrl = "http://localhost:4040/RyazMax/BaumanBotApi/1.0.0/";
	async function onClickSpec() {
		let url = `${baseUrl}hospital?spec=${specInp}`;
    	fetch(url).then((resp)=>{
      	if (resp.ok){
        	return resp.json();
      	}
      	throw Error("Error")
    	}).then((data)=>{
      		answer = JSON.parse(data)
    	}).catch((e)=>{
      		console.log(e)
    	})		
	}
	async function onClickName() {
		let url = `${baseUrl}hospital?name=${nameInp}`;
    	fetch(url).then((resp)=>{
      	if (resp.ok){
        	return resp.json();
      	}
      	throw Error("Error")
    	}).then((data)=>{
      		answer = JSON.parse(data)
    	}).catch((e)=>{
      		console.log(e)
    	})
	}
</script>
<style>
	.content {
		display: flex;
		flex-direction: row;
		margin-left: -15%;
		font-family: Comfortaa;
	}
	.result {
		margin-left: 20%;
		min-width: 550px;
		min-height: 500px;
		border: solid #1b1612 2px;
		border-radius: 15px;
	}
	button, input {
		font-family: Comfortaa;
		border-radius: 15px 15px 15px 15px;
		border-color: #1b1612;
		min-height: 30px;
		font-size: 20px;
		text-align: center;
	}
	button {
		color: #e8cba8;
		background-color: #1b1612;
	}
	.block-input {
		display: flex;
		flex-direction: row;
		margin-left: 0%;
	}
</style>

<svelte:head>
	<title>doctors</title>
</svelte:head>


<div class="content">
	<div style="margin-top: 50px; display: flex; flex-direction: column">
		
		<h1 style="text-align: center">Поиск по специальности</h1>
		<div class="block-input">
			<input bind:value={specInp} style="align-self: center" type="text" placeholder="Специальность">
			<button on:click={onClickSpec}>Искать</button>
		</div>
		<h1 style="padding-top: 25%; text-align: center">Поиск по имени врача</h1>
		<div class="block-input">
			<input bind:value={nameInp} type="text" placeholder="Фамилия И.О.">
			<button on:click={onClickName}>Искать</button>
		</div>

	</div>

	<div class="result">
    {#if answer}
    <table>
      <tr><th>Имя</th><th>Кабинет</th><th>Дата</th><th>Время</th></tr>
      {#each answer as unit}
        <tr>
          <td>{unit.name}</td>
          <td>{unit.aud}</td>
          <td>{unit.schedule[0].date}</td>
          <td>{unit.schedule[0].time}</td>
        </tr>
      {/each}
    </table>
    {/if}
	</div>
</div>