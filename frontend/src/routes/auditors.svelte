<script>
	let answer = "";
	let locInp = "ГЗ";
	let weektypeInp = "чс";
	let weekdayInp = "пн";
	let pairnumInp = "2";
  let baseUrl = "http://localhost:4040/RyazMax/BaumanBotApi/1.0.0/";
	async function onClickAud() {
		let url = `${baseUrl}audience?location=${locInp}&weektype=${weektypeInp}&weekday=${weekdayInp}&pairnum=${pairnumInp}`;
    	answer = url;
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
		margin-left: 30.8%;
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
		align-self: center;
		margin-top: 5%;
	}
	button {
		color: #e8cba8;
		background-color: #1b1612;
	}
</style>

<svelte:head>
	<title>auditors</title>
</svelte:head>


<div class="content">
	<div style="margin-top: 50px; display: flex; flex-direction: column; weight: 50%">
		
		<h1 style="text-align: center">Поиск пустой аудитории</h1>
		<input bind:value={locInp} type="text" placeholder="Корпус">
		<input bind:value={weekdayInp} type="text" placeholder="День">
		<input bind:value={pairnumInp} type="text" placeholder="Номер пары">
		<input bind:value={weektypeInp} type="text" placeholder="чс/зн">
		<button on:click={onClickAud}>Искать</button>

	</div>

	<div class="result">
	<ul>
  {#each answer as unit}
  <li> {unit.number} </li>
  {/each}
  </ul>
	</div>
</div>