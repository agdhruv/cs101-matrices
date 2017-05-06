$("#input_matrix").on("submit", function(e){
	e.preventDefault()
	valid = true
	for (var i = 1; i < 4; i++) {
		for (var j = 1; j < 4; j++) {
			elem = $("#input_matrix input[name=a" + i + j + "]")
			if(elem.val()== ''){
				valid = false
				break
			}
		}
	}
	if(valid){
		data = $(this).serialize()
		$.post("/api/threeByThree", data, function(response){
			if(response){
				determinant = response[0]
				transpose = response[1]
				inverse = response[2]
				square = response[3]
				$(".answers .determinant").html("<h2>Determinant</h2>" + determinant)
				$(".answers .transpose").html("<h2>Transpose</h2>" + transpose)
				$(".answers .inverse").html("<h2>Inverse</h2>" + inverse)
				$(".answers .square").html("<h2>Square</h2>" + square)
				$("p.error").html("")
			}
		});
	}
	else{
		$("p.error").html("Please fill in all values.");
		$(".answers .determinant").html("")
		$(".answers .transpose").html("")
		$(".answers .inverse").html("")
		$(".answers .square").html("")
	}
});

$("input[type=reset]").click(function(e){
	e.preventDefault()
	location.reload()
});