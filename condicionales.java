import java.util.Scanner;

public class condicionales {


    public static void main(String[] args) {
    
        

        Scanner leer= new Scanner ( System.in);
    
    int  opciones =leer.nextInt();
while (opciones >=1 && opciones <=5) {

    System.out.println( "Menu de opciones");
    System.out.println("1  personas"); 
    System.out.println("2 vehiculos");
    System.out.println("3universidades");
    System.out.println("4 notas");
    System.out.println("5 salir");
    System.out.println("seleccione una opcion");



        switch (opciones) {
           
            case 1:   System.out.println( "haz seleccionado la opcion personas");
        
                break;
            case 2: System.out.println(" haz selecionado la opcion vehiculos");
                break;
            case 3: System.out.println(" haz seleccionado la opcion universidades");
                break;
            case 4: System.out.println("haz selecionado la opcione notas ");
                break;
            case 5: System.out.println("haz selecionado la opciopn salir");
                break;

            default:  System.out.println(" haz, seleccionado una opcion incorrecta, seleciona nuevamente");
                break;
            
        }
    }


}
}