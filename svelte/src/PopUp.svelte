<!-- PopUp.svelte -->

<script>

    export let isVisible = false;
    // Define thresholds for color coding
    let impactThreshold = 1;
    
    

    import { setContext } from 'svelte';
    import { createEventDispatcher } from 'svelte';

    // Dispatch events to notify parent components
    const dispatch = createEventDispatcher();

    // Export context for child components to access the dispatch function
    setContext('dispatch', dispatch);

    let state = sessionStorage.getItem("state");
    let county = sessionStorage.getItem("county");
    let year = sessionStorage.getItem("disaster_year");
    let month = sessionStorage.getItem("disaster_month");

    let isDone = false;
    let housingCosts;

    let tableData = [
        { month: 'T - 12', homeValue: 100000, percentChange: 0},
        { month: 'T - 11', homeValue: 102000, percentChange: 2 },
        { month: 'T - 10', homeValue: 104040, percentChange: 3 },
        { month: 'T - 9', homeValue: 106120.80, percentChange: -1 },
        { month: 'T - 8', homeValue: 108243.22, percentChange: 2 },
        { month: 'T - 7', homeValue: 110408.08, percentChange: -2 },
        { month: 'T - 6', homeValue: 112616.24, percentChange: 2 },
        { month: 'T - 5', homeValue: 114868.56, percentChange: 2 },
        { month: 'T - 4', homeValue: 117165.93, percentChange: -8 },
        { month: 'T - 3', homeValue: 119509.25, percentChange: 2 },
        { month: 'T - 2', homeValue: 121899.43, percentChange: -9 },
        { month: 'T - 1', homeValue: 124337.42, percentChange: 2 },
        { month: 'T', homeValue: 126824.17, percentChange: -2 },
        { month: 'T + 1', homeValue: 129360.09, percentChange: 2 },
        { month: 'T + 2', homeValue: 131945.29, percentChange: 24 },
        { month: 'T + 3', homeValue: 134580.20, percentChange: 7 },
        { month: 'T + 4', homeValue: 134580.20, percentChange: 3 },
        { month: 'T + 5', homeValue: 134580.20, percentChange: 50 },
        { month: 'T + 6', homeValue: 134580.20, percentChange: -8 },
        { month: 'T + 7', homeValue: 134580.20, percentChange: 20 },
        { month: 'T + 8', homeValue: 134580.20, percentChange: 28 },
        { month: 'T + 9', homeValue: 134580.20, percentChange: 7 },
        { month: 'T + 10', homeValue: 134580.20, percentChange: 2 },
        { month: 'T + 11', homeValue: 134580.20, percentChange: 2 },
        { month: 'T + 12', homeValue: 134580.20, percentChange: 2 },
    ];
    fetch(`./search/${state}/${county}/${year}/${month}`)
        .then(response => response.json())
        .then(data => {
            housingCosts = data;
            for (let i = 0; i < 25; i++) {
                let i_month = housingCosts[i].month;
                let i_year = housingCosts[i].year;
                let i_hcosts = housingCosts[i].housing_cost;

                if (i != 0) {
                    let originalPrice = housingCosts[i - 1].housing_cost;
                    let newPrice = housingCosts[i].housing_cost;
                    console.log(`${newPrice} > ${originalPrice}`);
                    let percentChange = ((newPrice - originalPrice) / (originalPrice)) * 100;

                    tableData[i].percentChange = percentChange;
                }
                 tableData[i].homeValue = i_hcosts;
            }
            isDone = true;
        });


    // Function to determine cell color based on percent change
    function getCellColor(percentChange) {
        if (percentChange < impactThreshold) {
            return 'red'; // High impact color
        } else {
            return 'green'; // Low impact color
        }
    }

     // Function to recalculate cell colors when the threshold changes
    //  function recalculateCellColors() {
    // //     tableData.forEach(row => {
    // //         row.color = getCellColor(row.percentChange);
    // //     });
    // // }

 
    //     // Reactively recalculate cell colors when the threshold changes
    //     $: {
    //     recalculateCellColors();
    // }
    
    // Function to handle applying the threshold change
    // function applyThresholdChange() {
    //     recalculateCellColors();
    // }
</script>

{#if isVisible && isDone}
    <div class="popup">
        
        <button class="close-button" on:click={()=>isVisible=false}>Close</button>
        <div style="padding: 20px;">

            <div class="input-container">
                <label for="thresholdInput">Impact Threshold:</label>
                <input type="number" id="thresholdInput" bind:value={impactThreshold} min="0" step="1"/>
                <button on:click={applyThresholdChange}>Apply Change</button>
            </div>

            <table>
                <thead>
                    <tr>
                        <th>Month</th>
                        <th>Typical Home Value</th>
                        <th>% Change from Previous Month</th>
                    </tr>
                </thead>
                <tbody>
                    {#each tableData as row}
                        <tr>
                            <td>{row.month}</td>
                            <td>{row.homeValue}</td>
                            <td style="color: {getCellColor(row.percentChange)}">{row.percentChange}%</td>
                        </tr>
                    {/each}
                </tbody>
            </table>
        </div>
    </div>
{/if}

<style>
    .popup {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: white;
        width: auto; /* Set the width of the popup */
        height: auto; /* Set the height of the popup */
        border-radius: 10px; /* Round edges */
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); /* Shadow */
        z-index: 9999;
    }
    
    .close-button {
        position: absolute;
        bottom: 10px;
        right: 10px;
        cursor: pointer;
    }

    .input-container {
        display: flex;
        align-items: center;
    }

    .input-container label {
        margin-right: 10px;
    }
 table, td, tr {
        border: 1px solid black;
        border-collapse: collapse;
        
    }

</style>

