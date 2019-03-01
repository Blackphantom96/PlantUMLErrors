package co.edu.escuelaing.is.sbco.controller;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;
import com.mashape.unirest.request.body.MultipartBody;
import lombok.Data;
import org.projog.api.Projog;
import org.projog.api.QueryStatement;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.SessionScoped;
import javax.faces.context.FacesContext;
import javax.servlet.ServletContext;

import java.io.*;

@ManagedBean(name = "Front")
@SessionScoped
@Data
public class PlantUMLController {
    private String text ;
    Projog prolog ;

    public PlantUMLController(){

        text="@startuml\n" +
                "  class example\n" +
                "  example -- \"1\" example\n" +
                "@enduml";
    }

    public void Action() {
        prolog =new Projog();
        try {
            ServletContext servletContext = (ServletContext) FacesContext.getCurrentInstance().getExternalContext().getContext();
            try {
                File f = new File(servletContext.getRealPath("/resources/diagram.wsd"));
                FileWriter fw = new FileWriter(f);
                BufferedWriter out = new BufferedWriter(fw);
                out.write(text);
                out.flush();
                out.close();
                System.out.println(servletContext.getRealPath("/resources/diagram.wsd"));
                HttpResponse<String> x = Unirest.post("http://127.0.0.1:5001").field("file",new File(servletContext.getRealPath("/resources/diagram.wsd"))).asString();
                f = new File(servletContext.getRealPath("/resources/assert.pl"));
                fw = new FileWriter(f);
                out = new BufferedWriter(fw);
                out.write(x.getBody());
                out.flush();
                out.close();
                prolog.consultFile(new File(servletContext.getRealPath("/resources/project.pl")));
                QueryStatement sq = prolog.query("multiplicityError(X).");
            } catch (Exception ex) {
                ex.printStackTrace();
            }
            String[] temp = {servletContext.getRealPath("/resources/diagram.wsd")};
            Run.main(temp);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
