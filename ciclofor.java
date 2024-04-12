import java.util.*;

public class Actividad2 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Map<String, Object> vuelo = new HashMap<>();

        String aerolinea = "Avianca";
        String numVuelo = "AV3102";
        String origen = "Cartagena";
        String destino = "Medellin";
        List<String> tipoMaleta = Arrays.asList("Cabina", "Mano", "Bodega");


        vuelo.put("Aerolinea", aerolinea);
        vuelo.put("Vuelo", numVuelo);
        vuelo.put("Origen", origen);
        vuelo.put("Destino", destino);
        vuelo.put("Tipo_Maleta", tipoMaleta);

        
        System.out.println("Valores del diccionario:");
        System.out.println("Aerolinea: " + vuelo.get("Aerolinea"));
        System.out.println("Vuelo: " + vuelo.get("Vuelo"));
        System.out.println("Origen: " + vuelo.get("Origen"));
        System.out.println("Destino: " + vuelo.get("Destino"));

        System.out.println("\nTipo de Maleta:");
        for (String maleta : tipoMaleta) {
            System.out.println(maleta);
        }

        leer.close();
    }
}
