<script>
	export let segment;
</script>

<style>
	nav {
		font-weight: 300;
		padding: 0 1em;
		display: flex;
		height: 100px;
		background: linear-gradient(#e8cba8, #f1e4d4);
	}

	ul {
		margin: auto;
		padding: 0;
	}

	/* clearfix */
	ul::after {
		content: '';
		display: block;
		clear: both;
	}

	li {
		display: block;
		float: left;
	}

	[aria-current] {
		position: relative;
		display: inline-block;
	}

	[aria-current]::after {
		position: absolute;
		content: '';
		width: calc(100% - 1em);
		height: 2px;
		background-color: rgb(255,62,0);
		display: block;
		bottom: -1px;
	}

	a {
		text-decoration: none;
		padding: 1em 0.5em;
		display: block;
	}

	.logostyle {
		font-size: 20px;
		display: flex;
		flex-direction: column;
		padding: 0px;
		margin: 0px;
	} 	
	.logo1 {
		font-size: 45px;
		font-weight: 1000;
		padding: 5px;
		padding-top: 10px;
		padding-left: 50px;
		margin: 0px;
	}
	.logo2{
		font-size: 28px;
		font-weight: 1000;
		padding-top: 20px;
		padding-left: 50px;
		margin: -40px;
		align-self: center;
	}
	.choose {
		padding-right: 100px;
		font-size: 17px;
		font-weight: 1000;
	}

</style>

<nav>
	<div class="logostyle">
		<a href="." class="logo1">Shedule</a>
		<a href="." class="logo2">BMSTU</a>
	</div>
	<ul>
		<li class="choose"><a aria-current="{segment === 'classes' ? 'page' : undefined}" href="classes">пары</a></li>
		<li class="choose"><a aria-current="{segment === 'doctors' ? 'page' : undefined}" href="doctors">поликлиника</a></li>
		<li class="choose"><a aria-current="{segment === 'auditors' ? 'page' : undefined}" href="auditors">аудитории</a></li>
	</ul>
</nav>
