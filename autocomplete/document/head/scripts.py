#!/usr/bin/python
def render():
  print """\
    <!-- External scripts here -->
    <script src='./js/jquery.min.js'></script>
    <script src='./js/jquery-ui.min.js'></script>

    <!-- Local, in page javascript -->
    <script>
    $(document).ready(function() {
        $( "#queryField" ).autocomplete({
            source: "ajax/autocomplete.py",
            minLength: 2,
            select: function(event, ui) { 
                $("#queryField").val(ui.item.value);
                $("#queryForm").submit(); }
        });
    });
    </script>
  """
