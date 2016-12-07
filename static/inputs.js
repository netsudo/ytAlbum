$(document).ready(function() {
  $("#dropdown").change(function() {
      var selVal = $(this).val();
      if(selVal > 0) {
          for(var i = 1; i<= selVal; i++) {
              $("#inputDiv").append('<br><input id="titleVal" type="text" name="titleValue" value="" placeholder="Title" />');
              $("#inputDiv").append('<input id="timeVal" name="timeValue" value="" placeholder="Time" /><br>');
          }
      }
      else {
        $("#inputDiv").html('');
        $("#songTitle").html('');
        $("#timeTitle").html('');
      }
  });
});
