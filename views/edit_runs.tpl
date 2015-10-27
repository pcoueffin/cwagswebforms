<h1>Results so far:</h1>
<table border='1'>
<tr>
<td>Dog:</td>

<td>Date:</td>
<td>Level:</td>
<td>Result:</td>
%result = {}
%resultnum = {}
%resultids = []
%for row in results[0]:
%resultids.append(row['id'])
%resultnum = {row['id']:row['result']}
%runid = row['id']
%if resultnum[runid] == 1:
%resultnum[runid]="Pass"
%elif resultnum[runid]==0:
%resultnum[runid]="NQ"
%else:
%resultnum[runid] = "Not Scored Yet"
%end
    <tr>
      <td> {{row['name']}}</td>
      <td> {{row['date']}}</td>
      <td> {{row['level']}}</td>
      <td>{{resultnum[runid]}}</td>

    </tr>
%end
</table>



<h1>Enter more runs!</h1>
<h3>For each night of the league, there will be several runs. Judges are still TBA, but we will do our best to accomodate anyone who needs that second judge to title.
Prices:
$18 for any single run.
$16 per run if you sign up for at least 10 runs.
$15 per run if you sign up for all the remaining runs.
I will send you an invoice upon receiving your entry, with a total!

<form action="{{action}}" method="POST">
%rows7 = []
%rows9 = []
%rows8 = []
%rows10 = []
  %for event in results[1]:

  %if event['event_id'] == 7:
  %rows7.append(event)
  %end
   %if event['event_id'] == 8:
  %rows8.append(event)
  %end
   %if event['event_id'] == 9:
  %rows9.append(event)
  %end
   %if event['event_id'] == 10:
  %rows10.append(event)
  %end
  %end


   <h2>Nov 6, 2015</h2>
  <table style="text-align:center" border="1">
  <tr>
     <td>Event date: </td>
      <td>Level: </td>
      <td>Round number: </td>
      <td>Registered?</td>
      </tr>
  %for row in rows7:


    <tr>
      <td> {{row['date']}}</td>
      <td> {{row['level']}}</td>
      <td>{{row['idx']}}</td>
      <td>
	<input type="checkbox"  size="0" id="7" name="{{row['id']}}" value="{{row['id']}}"/>
      </td>
    </tr>

    %end


</table>


    <h2>Nov 20, 2015</h2>
   <table style="text-align:center" border="1">
      <tr>
     <td>Event date: </td>
      <td>Level: </td>
      <td>Round number: </td>
      <td>Registered?</td>
      </tr>
       %for row in rows8:

    <tr>
      <td> {{row['date']}}</td>
      <td> {{row['level']}}</td>
      <td>{{row['idx']}}</td>
      <td>
	<input type="checkbox"  size="0" id="7" name="{{row['id']}}" value="{{row['id']}}"/>
      </td>
    </tr>
    %end


</table>


    <h2>Nov 27, 2015</h2>
  <table style="text-align:center" border="1">
      <tr>
     <td>Event date: </td>
      <td>Level: </td>
      <td>Round number: </td>
      <td>Registered?</td>
      </tr>
      %for row in rows9:

    <tr>
      <td> {{row['date']}}</td>
      <td> {{row['level']}}</td>
      <td>{{row['idx']}}</td>
      <td>
	<input type="checkbox"  size="0" id="7" name="{{row['id']}}" value="{{row['id']}}"/>
      </td>
    </tr>
    %end

</table>


    <h2>Dec 18, 2015</h2>
   <table style="text-align:center" border="1">
          <tr>
     <td>Event date: </td>
      <td>Level: </td>
      <td>Round number: </td>
      <td>Registered?</td>
      </tr>
      %for row in rows10:

    <tr>
      <td> {{row['date']}}</td>
      <td> {{row['level']}}</td>
      <td>{{row['idx']}}</td>
      <td>
	<input type="checkbox"  size="0" id="7" name="{{row['id']}}" value="{{row['id']}}"/>
      </td>
    </tr>
%end

</table>
<br>

<input type="submit" name="save" value="save" style="width: 100px; height: 100px">
</form>
