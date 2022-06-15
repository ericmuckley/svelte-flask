<script>
  let rand = -1;

  function getRandomNumber() {
    fetch("./geetrandomnumber").then(d => d.text()).then(d => (rand = d))
  }
</script>


<h1>Your number is {rand}!</h1>
<button on:click={getRandomNumber}>Get a random number</button>