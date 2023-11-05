
<script>
    function myFunction() {
        $.ajax({
            type: "GET",
            url: "/watch-views/",
            success: function(data) {
                $('#viewCount1').html(data.current_views);
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    }

    // Call the function initially
<!--    myFunction();-->

<!--    setInterval(myFunction, 1200000);-->

<!--    function setRandomInterval() {-->
<!--        var randomInterval = Math.floor(Math.random() * (30000 - 10000 + 1)) + 10000; // Generates a random number between 10000 and 90000-->
<!--        setInterval(function() {-->
<!--            myFunction();-->
<!--            setRandomInterval(); // After each random interval, reset the interval-->
<!--        }, randomInterval);-->
<!--    }-->

<!--    // Call the random interval function to start the process-->
<!--    setRandomInterval();-->
</script>
