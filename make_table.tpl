%#template to generate a HTML table from a list of tuples
%#(or list of lists, or tuple of tuples or ...)
%dict_for_results = {0: "NQ", 1: "Pass", None:"Not yet scored"}
<table border="1">
%hdr=None
%for row in rows:

  %if not hdr:
  %  hdr=row.keys()

  <tr>
    %for key in hdr:
      <th>{{key.title()}}</th>
    %end
  </tr>
  %end
  <tr>
    %for col in hdr:
    %if col == "result":
    %resultvalue = row[col]
    %row[col] = dict_for_results[resultvalue]
    %end
    <td>{{row[col]}}</td>
    %end
  </tr>
%end
</table>
