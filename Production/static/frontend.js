function annotations() {
	if ($("#checkbox").prop('checked') == false) {
		$(checkbox).prop('checked', true);
		var y = document.getElementsByTagName("satire");
		for (i = 0; i < y.length; i++) {
  	y[i].style.backgroundColor = "skyblue";
	}
	} else {
		$(checkbox).prop('checked', false);
		var y = document.getElementsByTagName("satire");
		for (i = 0; i < y.length; i++) {
  	y[i].style.backgroundColor = "white";
	}
	}
}

function search() {
	var keyword = document.getElementById('keyword').value;
	location.href = '/search?keyword=' + keyword;
}