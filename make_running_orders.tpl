%#template to generate a HTML table from a list of tuples 
%#(or list of lists, or tuple of tuples or ...)
<table border="1">
%rounds = []
%hdr=None

%for row in rows:
  %  hdr=row.keys()
  %round = row['round']
  %level = row['level']

  %if round not in rounds:

  %tabletitle = "Round "+str(round-22)+" Level "+str(level)
  %createnewtablecode = "</table><h1>"+tabletitle+"</h1><table border=\"1\">"

  {{!createnewtablecode}}



    <tr>
      %for key in hdr:
      <th>{{key.title()}}</th>
      %end
  </tr>
  %end

  <tr>
  %for key in hdr:
  <td>{{row[key]}}</td>
  %end
  </tr>

  %rounds.append(round)
%print rounds
%end
</table>

