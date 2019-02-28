package co.edu.escuelaing.is.sbco.controller;

import lombok.Data;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.SessionScoped;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

@ManagedBean(name = "Front")
@SessionScoped
@Data
public class PlantUMLController {
    private String text ;

    public PlantUMLController(){
        text="";
    }

    public void Action() {
        try {
            File f = new File("/Users/juanmoreno/Dev/SBCO/Prolog/WebApp/src/main/webapp/resources/images/diagram.wsd");
            try {
                FileWriter fw = new FileWriter(f);
                BufferedWriter out = new BufferedWriter(fw);
                out.write(text);
                out.flush();
                out.close();
            } catch (Exception ex) {
                ex.printStackTrace();
            }
            String[] temp = {"/Users/juanmoreno/Dev/SBCO/Prolog/WebApp/src/main/webapp/resources/images/diagram.wsd"};
            Run.main(temp);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
