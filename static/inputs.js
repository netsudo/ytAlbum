$(document).ready(function() {
  $("#dropdown").change(function() {
      var selVal = $(this).val();
      if(selVal > 0) {
          $("#songTitle").html('<h4>Titles:</h4>');
          $("#timeTitle").html('<h4>Times:</h4>')
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
