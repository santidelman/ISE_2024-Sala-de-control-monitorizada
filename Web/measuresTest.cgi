t <html><head><title>Test Ambiental</title>
t <meta http-equiv="refresh" content="5"></head>
i pg_header.inc
t 	<tr style="background-image:url(fondo.png);"><th>
t 		<div style="width:900;">
t 			<div style="height: 10;"></div>
t 			<table style="font-family:Verdana; margin:10;" align="right">
t 				<tr>
t 					<td>Hora</td>
c z 1 				<td><input type=text name=rtc1 size=20 maxlength=20 value="%s"></td>
t 				</tr>
t 				<tr>
t 					<td>Fecha</td>
c z 2 				<td><input type=text name=rtc2 size=20 maxlength=20 value="%s"></td>
t 				</tr>
t 			</table>
t 			<div style="height: 50;"></div>
t 			<p style="font-size: 30;"><b>Lectura de Condiciones Ambientales</b></p>
t 			<center><table style="font-family:Verdana; margin:10;">
t 				<tr padding="5">
t 					<td width="60" valing="top"><img src="temp.png" width="50" height="50"></td>
t  					<th style="width:200; text-align:left;">Temperatura:</th>
t  					<th style="width:250; text-align:center;">**</th>
t  					<th style="width:200; text-align:right;"><input type=button value="Actualizar" background-color:"#E9E9E9"></th>
t 				</tr>
t 				<tr padding="5">
t 					<td width="60" valing="top"><img src="humedad.png" width="50" height="50"></td>
t  					<th style="width:200; text-align:left;">Humedad:</th>
t  					<th style="width:250"; text-align:center;>**</th>
t  					<th style="width:200; text-align:right;"><input type=button value="Actualizar" background-color:"#E9E9E9"></th>
t 				</tr>
t 				<tr padding="5">
t 					<td width="60" valing="top"><img src="co2.png" width="50" height="50"></td>
t  					<th style="width:200;; text-align:left;">Monoxido de Carbono</th>
t  					<th style="width:300; text-align:center;">**</th>
t  					<th style="width:200; text-align:right;"><input type=button value="Actualizar" background-color:"#E9E9E9"></th>
t 				</tr>
t 			</table></center>
#t			<input type=button value="&nbsp;&nbsp;OFF&nbsp;&nbsp;" background-color:"#007BFF">
t 		</div>
t </th></tr>
t <p align=center>
t <input type=button value="Refresh" onclick="updateMultiple(formUpdate,plotRTCGraph)">
t Periodic:<input type="checkbox" id="adChkBox" onclick="periodicUpdateRTC()">
t </p>
i pg_footer.inc
. End of script must be closed with period.
