<script>
  	import PopUp from './PopUp.svelte';

	// Code for fetching the key from Flask backend
	let key = '';
	let googleMapsReady = false;
	fetch('./key')
		.then(k => k.text())
		.then(k => {
			key = k;
			googleMapsReady = true
		});
	let state = '';
	// county ex. Montgomery
	let county = '';
	// month format "XX", ex. Jan -> 01, Feb -> 02, etc.
	let startMonth = '';
	// year format "XXXX"
	let startYear = '';
	let endMonth = '';
	let endYear = '';
	let k=name.toUpperCase();
	//importing pop up from the svelete 
	let popUpVisible =false;

	async function getDisasterData() {
		const response = await fetch(`./search/${state}/${county} (County)/${startYear}/${startMonth}/${endYear}/${endMonth}`);
		const disasters = await response.json();

		sessionStorage.setItem("state", state);
		console.log(sessionStorage.getItem("state"));
        sessionStorage.setItem("county", county);

		let countyFIPS = `${disasters[0].state_fips_code}${disasters[0].county_fips_code}`
		let response1 = await fetch(`./latlng/${countyFIPS}`);
		let coords = await response1.text();
		coords = coords.split(' ');

		let latitude = parseFloat(coords[1]);
		let longitude = parseFloat(coords[0]);
		let map = new google.maps.Map(document.getElementById('map'), {
			zoom: 4,
			center: { lat: latitude, lng: longitude },
		});

		let name = disasters[0].disaster_name;
		let year = disasters[0].year;
		let month = disasters[0].month;

		sessionStorage.setItem("disaster_year", year);
		sessionStorage.setItem("disaster_month", month);

		const marker = new google.maps.Marker({
			position: { lat: latitude, lng: longitude },
			title: name,
		});
		google.maps.event.addListener(marker, 'click', () => {
			popUpVisible = !popUpVisible
		});					
		marker.setMap(map);
	}
</script>

<svelte:head>
	{ #if googleMapsReady }
	<!-- TODO: fix loading key from backend -->
	<script defer async src="https://maps.googleapis.com/maps/api/js?key={key}&callback=initMap"></script>
	{/if}
</svelte:head>

{ #if googleMapsReady }
<div id="parent" style="background-color: none; display:flex; justify-content: center; height:6%; border:none">
	<input bind:value={state} placeholder="Enter state (e.g. MD)" />
	<input bind:value={county} placeholder="Enter county (e.g. Montgomery" />
	<input bind:value={startMonth} placeholder="Enter start month (XX)" />
	<input bind:value={startYear} placeholder="Enter start year (XXXX)" />
	<input bind:value={endMonth} placeholder="Enter end month (XX)" />
	<input bind:value={endYear} placeholder="Enter end year (XXXX)" />		  
	<div id = "search button" style="background-color:none; display:flex; justify-content: reverse-end; height:80%" >              
		<button disabled={!(state && (startMonth && startYear) && (endMonth && endYear))} on:click={getDisasterData}>Search</button>
		<style>
      		button{
        		background-color: #f69697;
				border: none;
				text-align: center;
				text-decoration: none;
				display: inline-block;
				font-size: 16px;
				margin: 4px 2px;
				cursor: pointer;
			}
      	</style>
	</div>
</div>
{/if}

{#if popUpVisible}
<PopUp isVisible={popUpVisible} />
{/if}


<style>
	.full-screen {
		width: 100vw;
		height: 100vh;
	}
</style>

<div class='full-screen' id='map'></div>