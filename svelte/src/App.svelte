<script>
	import Map from './Map.svelte'
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
	let county = '';
	let state = '';
	let start_year_date = '';
	let end_year_date = '';
	let k=name.toUpperCase();

	function sendRequest(){
		// retrive strings
		// send strings to flask backend
		// receive json data from backend
		// load as google maps pins
		if (start_year_date==null||end_year_date==null){
			
		}
	}
</script>

<svelte:head>
	<!-- TODO: fix loading key from backend -->
	<!-- { #if googleMapsReady } -->
	<script defer async
		src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAGSkMd2TxcUsrY3ZTcEESTXKk15uwbklg&callback=initMap">
	</script>
	<!-- { /if} -->
</svelte:head>	
	<div id="parent" style="background-color: none; display:flex; justify-content: center; height:6%; border:none">
		<input bind:value={state} placeholder="state" />
		<input bind:value={county} placeholder="county" />
		<input bind:value={start_year_date} placeholder="start-year/date" />
		<input bind:value={end_year_date} placeholder="end-year/date" />
		<div id = "search button" style="background-color:none; display:flex; justify-content: reverse-end; height:80%" >              
			<button disabled={!(state && start_year_date && end_year_date)} on:click = {giveData}>Search</button>
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
<style>
:global(body) {
	padding: 0;
}
</style>

{ #if ready }
<Map></Map>
{ /if }
