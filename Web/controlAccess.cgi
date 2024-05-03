t <html><head><title>Historial de Acceso
t <script>
t function agregarMedicion(temperatura) {
t 	var tabla = document.getElementById("measuresTable");
t   var nuevaFila = tabla.insertRow(-1);
t   var celdaHora = nuevaFila.insertCell(0);
t   var celdaTemperatura = nuevaFila.insertCell(1);
t   var celdaCO2   = nuevaFila.insertCell(2);
t   var celdaFecha  = nuevaFila.insertCell(3);
t   var celdaTemperatura = nuevaFila.insertCell(4);
t   var fechaActual  = new Date();
t   celdaHora.innerHTML = fechaActual.toLocaleTimeString();
t   celdaTemperatura.innerHTML = temperatura;
t }
t function simularRecepcionDatos() {
t   var temperaturaSimulada = Math.random() * 20 + 10; // Temperatura entre 10 y 30 grados Celsius
t   agregarMedicion(temperaturaSimulada.toFixed(2));
t   var humedadSimulada = Math.random() * 50 + 30;    // Humedad entre 30% y 80%
t   var co2Simulado = Math.random() * 400 + 200;      // CO2 entre 200 ppm y 600 ppm
t   agregarMedicion(temperaturaSimulada.toFixed(2), humedadSimulada.toFixed(2), co2Simulado.toFixed(2));
t }
t function periodicUpdateAd() {
t  if(document.getElementById("adChkBox").checked == true) {
t 	simularRecepcionDatos();
t   ad_elTime = setTimeout(periodicUpdateAd, formUpdate.period);
t  }
t  else
t   clearTimeout(ad_elTime);
t }
t </script>
t </title></head>
i pg_header.inc
t 	<tr style="background-image:url(fondo.png);"><th>
t 		<div style="width:900;>
t 			<div style="height: 25;"></div>
t 			<p style="font-size: 30;"><b>Historial de Acceso</p>
t 			<center><table id="accessTable" style="font-family:Verdana; margin:10;">
t 				<tr padding="5">
t 					<td width="60" valing="top" align="middle"><img src="uid.png" width="50" height="50"></td>
t 					<td width="60" valing="top" align="middle"><img src="programador.png" width="50" height="50"></td>
t 				</tr>
t 				<tr padding="5">
t  					<th style="width:200; text-align:center;">UID</th>
t  					<th style="width:200; text-align:center;">Usuario</th>
t  					<th style="width:200;; text-align:center;">Hora de entrada</th>
t  					<th style="width:200"; text-align:center;">Hora de salida</th>
t 				</tr>
t 			</table></center>
t 		</div>
t </th></tr>
i pg_footer.inc
. End of script must be closed with period.

