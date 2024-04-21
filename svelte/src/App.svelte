<script>
<<<<<<< Updated upstream
	import Map, map from './Map.svelte'
=======
  import Map from './Map.svelte'
  import PopUp from './PopUp.svelte';
>>>>>>> Stashed changes
	export let ready

	// Code for fetching the key from Flask backend
	// let key = '';
	// let googleMapsReady = false;
	// function getKey() {
	// 	fetch('./key')
	// 		.then(k => {
	// 			googleMapsReady = true;
	// 			key = k;
	// 		});9
	// }
	// getKey();
	// console.log(key)
	let state = '';
<<<<<<< Updated upstream
	let county = '';
	// month format "XX", ex. Jan -> 01, Feb -> 02, etc.
	let startMonth = '';
	// year format "XXXX"
	let startYear = '';
	let endMonth = '';
	let endYear = '';
	let k=name.toUpperCase();

	function getDisasterData(state, county, startMonth, startYear, endMonth, endYear) {
		const json = '';
		fetch(`./search/${state}/${county}/${startYear}/${startMonth}/${endYear}/${endMonth}`)
			.then(d => (json = d));
		const disastersData = JSON.parse(json);
		for (const obj in disastersData) {
			// State fips, county fips
			let stateFIPS = obj.state_fips_code;
			let countyFIPS = obj.county_fips_code;
			// Get place ID w/ fips code
			const headers = {
				'X-Goog-Api-Key': 'AIzaSyAGSkMd2TxcUsrY3ZTcEESTXKk15uwbklg',
			};
			const lookupRegionRequest = {
				search_values: [
					{
						'unit_code': stateFIPS + countyFIPS,
						'place_type': 'ADMINISTRATIVE_AREA_LEVEL_2',
						'region_code': 'US',
					},
				],
			};
			const response = await regionLookupClient.searchRegion({ headers, data });
			// Place marker
			const marker = new google.maps.marker.AdvancedMarkerElement({
				map,

			})
		}
		// center map on state
		
		// Montgomery County, MD --> 24031
		// look up place ID based on 

	}
=======
	let start_year_date = '';
	let end_year_date = '';

	// function sendRequest(){
	// 	// retrive strings
	// 	// send strings to flask backend
	// 	// receive json data from backend
	// 	// load as google maps pins
	// }


  //importing pop up from the svelete 
	let popUpVisible =false;
  

	function togglePopUp(){
		popUpVisible=!popUpVisible;

	}

>>>>>>> Stashed changes
</script>

<svelte:head>
	<!-- TODO: fix loading key from backend -->
	<script defer async src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAGSkMd2TxcUsrY3ZTcEESTXKk15uwbklg&callback=initMap"></script>
</svelte:head>

<style>
	:global(body) {
		padding: 0;
	}
	</style>

<<<<<<< Updated upstream
<div id="parent" style="background-color: none; display:flex; justify-content: center; height:6%; border:none">
	<input bind:value={state} placeholder="Enter state (e.g. MD)" />
	<input bind:value={county} placeholder="Enter county (e.g. Montgomery" />
	<input bind:value={startMonth} placeholder="Enter start month (XX)" />
	<input bind:value={startYear} placeholder="Enter start year (XXXX)" />
	<input bind:value={endMonth} placeholder="Enter end month (XX)" />
	<input bind:value={endYear} placeholder="Enter end year (XXXX)" />
	<div id = "search button" style="background-color:none; display:flex; justify-content: reverse-end; height:80%" >              
		<button disabled={!(state && (startMonth && startYear) && (endMonth && endYear))} onclick={}>Search</button>
=======
<div class="parent" style="background-color: none; display:flex; justify-content: center; height:6%; border:none">
	<input bind:value={state} placeholder="state" />
	<input bind:value={county} placeholder="county" />
	<input bind:value={start_year_date} placeholder="start-year/date" />
	<input bind:value={end_year_date} placeholder="end-year/date" />
  
  
  <button on:click = {togglePopUp}> 
    Open PopUp</button>
  <!-- svelte-ignore missing-declaration -->
  {#if popUpVisible}
  <PopUp isVisible={popUpVisible} />
  {/if}

  
  
	<div id = "search button" style="background-color:none; display:flex; justify-content: reverse-end; height:80%" >              
    <button disabled={!(state && start_year_date && end_year_date)}>Search</button>
>>>>>>> Stashed changes
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



{ #if ready }
<Map></Map>
{ /if }
