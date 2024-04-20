<script>

	let rand = -1;
	// send requests to Flask backend with fetch()
	// gets the value returned by the specified route (e.g. rand)
	function getRand() {
	  fetch("./rand")
		.then(d => d.text())
		.then(d => (rand = d));
	}

  (g=>{var h,a,k,p="The Google Maps JavaScript API",c="google",l="importLibrary",q="__ib__",m=document,b=window;b=b[c]||(b[c]={});var d=b.maps||(b.maps={}),r=new Set,e=new URLSearchParams,u=()=>h||(h=new Promise(async(f,n)=>{await (a=m.createElement("script"));e.set("libraries",[...r]+"");for(k in g)e.set(k.replace(/[A-Z]/g,t=>"_"+t[0].toLowerCase()),g[k]);e.set("callback",c+".maps."+q);a.src=`https://maps.${c}apis.com/maps/api/js?`+e;d[q]=f;a.onerror=()=>h=n(Error(p+" could not load."));a.nonce=m.querySelector("script[nonce]")?.nonce||"";m.head.append(a)}));d[l]?console.warn(p+" only loads once. Ignoring:",g):d[l]=(f,...n)=>r.add(f)&&u().then(()=>d[l](f,...n))})({
    key: "YOUR_API_KEY",
    v: "weekly",
    // Use the 'v' parameter to indicate the version to use (weekly, beta, alpha, etc.).
    // Add other bootstrap parameters as needed, using camel case.
  });

	let county = '';
	let state = '';
	let start_year_date = '';
	let end_year_date = '';
	let k=name.toUpperCase();

	function giveData(){
		if (start_year_date==null||end_year_date==null){
			
		}
	}	
  
  </script>
    
  

    <div id="parent" style="background-color: none; display:flex; justify-content: center; height:6%; border:none">
      <input bind:value={state} placeholder="state" />
    <input bind:value={county} placeholder="county" />
    <input bind:value={start_year_date} placeholder="start-year/date" />
    <input bind:value={end_year_date} placeholder="end-year/date" />
    
      <div id = "search button" style="background-color:none; display:flex; justify-content: reverse-end; height:80%" >
                             
        <button disabled={!(state && start_year_date && end_year_date)} on:click = {giveData}>
          Search
        </button>
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
    
    <div id="mapArea" style="display:flex; height:100%; border:none">
      
      
    <p>THIS IS MAP!</p>
    
    </div>
    
    









