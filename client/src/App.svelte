<script>
  let rand = -1;
  let items = [];

  function getRandomNumber() {
    fetch("./getrandomnumber").then(r => r.text()).then(r => (rand = r))
  }

  /*
  function getItems() {
	fetch("./getitems").then(r => r.json()).then(r => (items = r))
  }

  function deleteItem() {
	this.parentElement.remove()
  }
  */
</script>


<h1>Your number is {rand}!</h1>

<button class="btn btn-primary mt-3" type="button" on:click={getRandomNumber}>
	Get a random number
</button>

<!--
<button class="btn btn-secondary mt-3" type="button" on:click={getItems}>
	Get items
</button>

<div class="mt-3">

	{#each items as item}
		<div class="my-1 d-flex w-50 justify-content-between">
			<div class="d-flex">
				<b>{item.name}</b> <span class="badge bg-secondary">{item.age} yrs old</span>: {item.occupation}			
			</div>

			<button class="btn btn-danger" on:click={deleteItem}>Delete</button>
		</div>
  	{/each}
</div>
-->