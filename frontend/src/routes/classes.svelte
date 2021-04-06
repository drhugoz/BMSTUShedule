<script>
	let baseUrl = "http://localhost:4040/RyazMax/BaumanBotApi/1.0.0/"
	let answer = "";
	let groupInp = "ИУ7-72Б";
	let teacherInp = "Рудаков И. В.";
  let pos = 0;
  let days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
	async function onClickGroup() {
		let url = `${baseUrl}group?name=${groupInp}`;
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
	async function onClickTeacher() {
		let url = `${baseUrl}professor?name=${teacherInp}`;
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
  function onClickForw() {
		pos = (pos + 1) % 6
	}
  function onClickBack() {
		pos = (pos + 5) % 6
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
		min-height: 450px;
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
	.block-nav {
		display: flex;
		flex-direction: row;
		align-self: center;
		margin-left: 40%;
	}
</style>

<svelte:head>
	<title>classes</title>
</svelte:head>


<div class="content">
	<div style="margin-top: 50px; display: flex; flex-direction: column;">
		
		<h1 style="text-align: center">Поиск по группе</h1>
		<div class="block-input">
			<input bind:value={groupInp} style="align-self: center" type="text" placeholder="Номер группы">
			<button on:click={onClickGroup}>Искать</button>
		</div>
		<h1 style="padding-top: 25%; text-align: center">Поиск по преподавателю</h1>
		<div class="block-input">
			<input bind:value={teacherInp} type="text" placeholder="Фамилия И.О.">
			<button on:click={onClickTeacher}>Искать</button>
		</div>
	</div>

	<div style="display: flex; flex-direction: column;">
	<div class="result">
		{#if answer && !answer.name}
			<table>
			<caption>{days[pos]}</caption>
			<tr><th>Числитель</th><th>Знаменатель</th><th>Начало</th><th>Конец</th></tr>
			{#each answer[pos] as unit}
				<tr>
				<td>{unit.oddweek.name} {unit.oddweek.location}</td>
				<td>{unit.evenweek.name} {unit.evenweek.location}</td>
				<td>{unit.oddweek.from}</td>
				<td>{unit.oddweek.to}</td>
				</tr>
			{/each}
			</table>
			{:else if answer}
			<table>
			<caption>{days[pos]}</caption>
			<tr><th>Числитель</th><th>Знаменатель</th><th>Начало</th><th>Конец</th></tr>
			{#each answer.schedule[pos] as unit}
				<tr>
				<td>{unit.oddweek.name} {unit.oddweek.location}</td>
				<td>{unit.evenweek.name} {unit.evenweek.location}</td>
				<td>{unit.oddweek.from}</td>
				<td>{unit.oddweek.to}</td>
				</tr>
			{/each}
			</table>
		{/if}
	</div>
	<div class="block-nav">
		<button on:click={onClickBack}>Назад</button>
		<button on:click={onClickForw}>Вперед</button>
	</div>
	</div>

</div>