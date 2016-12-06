$(document).ready(function() {
  $("#dropdown").change(function() {
      var selVal = $(this).val();
      if(selVal > 0) {
          $("#songTitle").html('<h5>Titles:</h5>');
          $("#timeTitle").html('<h5>Times:</h5>')
          for(var i = 1; i<= selVal; i++) {
              $("#inputDiv").append('<br><input id="titleVal" type="text" name="titleValue" value="" />');
              $("#inputDiv").append('<input id="timeVal" name="timeValue" value="" /><br>');
          }
      }
      else {
        $("#inputDiv").html('')
        $("#songTitle").html('')
        $("#timeTitle").html('')
      }
  });
});
