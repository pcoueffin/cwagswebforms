<h1> You've registered on the database!
Please make sure the Owner number in the dog table matches the ID number in the Person table.
If there are any errors, please email me at licketysit@gmail.com before resubmitting.
</h1>

<h2>Person Information</h2>
<table border="1">
%row = verify.next()
  %  hdrperson =['Name', 'disabilities', 'phone', 'address', 'email', 'id']
  % hdrdog = ['Dog', 'breed','reactivity', 'cwags', 'owner', 'DogId']
  %  values = row.values()
   <tr>
      %for key in hdrperson:
      <th>{{key.title()}}</th>
      %end
  </tr>

  <tr>
  %for key in hdrperson:
  %cellvalue = row[key]
  <td>{{cellvalue}}</td>
  %end
  </tr>
</table>
<h2> Dog Information</h2>

<table border="1">
   <tr>
      %for key in hdrdog:
      <th>{{key.title()}}</th>
      %end
  </tr>

  <tr>
  %for key in hdrdog:
  %cellvalue = row[key]
  <td>{{cellvalue}}</td>
  %end
  </tr>

</table>

<br><br>

<a href="http://cwags.pythonanywhere.com/dog/{{row['DogId']}}">Click here to select which runs to enter for this dog: {{row['Dog']}}</a>