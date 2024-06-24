import com.sun.mail.smtp.SMTPTransport;

import javax.activation.DataHandler;
import javax.activation.DataSource;
import javax.activation.FileDataSource;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Multipart;
import javax.mail.Session;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeMultipart;
import java.io.*;
import java.util.*;

public class SendEmailAttachment
{
    private static final String DIR = System.getProperty("user.dir");
    private static final String SMTP_HOST = "smtp2.nexcloud.id";
    private static final Integer SMTP_PORT = 587;
    private static final String USERNAME = "nd601.noreply@nexcloud.id";
    private static final String PASSWORD = "ND06011018";

    private static final String EMAIL_FROM = "sales@nexsoft.co.id";
    private static final String EMAIL_TO = getEmailTo(DIR + "/src/EMAIL_TO.txt");
    private static final String EMAIL_TO_CC = "";
    private static final String EMAIL_TO_BCC = getEmailToBcc(DIR + "/src/EMAIL_TO_BCC.txt");

    private static final String EMAIL_SUBJECT = getEmailSubject(DIR + "/src/EMAIL_SUBJECT.txt");
    private static final String EMAIL_TEXT = getEmailText(DIR + "/src/EMAIL_TEXT.txt");

    private static final String EMAIL_ATTACHMENT = getEmailAttachment(DIR + "/src/EMAIL_ATTACHMENT.txt");
    private static final String EMAIL_IMAGE = getEmailAttachment(DIR + "/src/EMAIL_IMAGE_PATH.txt");

    public static void main(String[] args)
    {
        Properties prop = System.getProperties();
        prop.put("mail.smtp.auth", "true");

        Session session = Session.getInstance(prop, null);
        Message msg = new MimeMessage(session);

        try
        {
            msg.setFrom(new InternetAddress(EMAIL_FROM));

            msg.setRecipients(Message.RecipientType.BCC,
                    InternetAddress.parse(EMAIL_TO_BCC, false));
//            msg.setRecipients(Message.RecipientType.TO,
//                    InternetAddress.parse(EMAIL_TO, false));

            msg.setSubject(EMAIL_SUBJECT);

            // text
            MimeBodyPart p1 = new MimeBodyPart();
            p1.setText(EMAIL_TEXT);

            // HTML email
            MimeBodyPart d1 = new MimeBodyPart();
            d1.setDataHandler(new DataHandler(new HTMLDataSource(EMAIL_TEXT)));
//            msg.setDataHandler(new DataHandler(new HTMLDataSource(EMAIL_TEXT)));

            // file
            MimeBodyPart p2 = new MimeBodyPart();
            FileDataSource fds = new FileDataSource(EMAIL_ATTACHMENT);
            p2.setDataHandler(new DataHandler(fds));
            p2.setFileName(fds.getName());

            // image
            MimeBodyPart p3 = new MimeBodyPart();
            FileDataSource fdsImage = new FileDataSource(EMAIL_IMAGE);
            p3.setDataHandler(new DataHandler(fdsImage));
            p3.setFileName(fdsImage.getName());

            Multipart mp = new MimeMultipart();
//            mp.addBodyPart(p1); /* using plain text as body email */
            mp.addBodyPart(d1); /* using html as body email */
            mp.addBodyPart(p2); /* use attachment file */
//            mp.addBodyPart(p3); /* use image as attachment or inline image */

            msg.setContent(mp);


            SMTPTransport t = (SMTPTransport) session.getTransport("smtp");

            // connect
            t.connect(SMTP_HOST, SMTP_PORT, USERNAME, PASSWORD);

            // send
            t.sendMessage(msg, msg.getAllRecipients());

            System.out.println("Response: " + t.getLastServerResponse());

            t.close();

        }
        catch (MessagingException e)
        {
            e.printStackTrace();
        }
    }

    public static String getEmailTo(String path)
    {
        String filename = path;
        List<String> list = new ArrayList<>();
        Scanner sc = null;
        try
        {
            sc = new Scanner(new File(filename));
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }
        List<String> lines = new ArrayList<String>();
        while (sc.hasNextLine()) {
            lines.add(sc.nextLine());
        }
        String[] arr = lines.toArray(new String[0]);
        String EMAIL_TO = Arrays.toString(arr).replace("[","").replace("]","");
        return EMAIL_TO;
    }

    public static String getEmailToBcc(String path)
    {
        String filename = path;
        List<String> list = new ArrayList<>();
        Scanner sc = null;
        try
        {
            sc = new Scanner(new File(filename));
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }
        List<String> lines = new ArrayList<String>();
        while (sc.hasNextLine()) {
            lines.add(sc.nextLine());
        }
        String[] arr = lines.toArray(new String[0]);
        String EMAIL_TO_BCC = Arrays.toString(arr).replace("[","").replace("]","");
        return EMAIL_TO_BCC;
    }

    public static String getEmailText(String path)
    {
        String filename = path;
        String EMAIL_TEXT = null;
        try
        {
            EMAIL_TEXT = new Scanner(new File(filename)).useDelimiter("\\Z").next();
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }
        return EMAIL_TEXT;
    }

    public static String getEmailSubject(String path)
    {
        String filename = path;
        String EMAIL_SUBJECT = null;
        try
        {
            EMAIL_SUBJECT = new Scanner(new File(filename)).useDelimiter("\\Z").next();
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }
        return EMAIL_SUBJECT;
    }

    public static String getEmailAttachment(String path)
    {
        String filename = path;
        String EMAIL_ATTACHMENT = null;
        try
        {
            EMAIL_ATTACHMENT = new Scanner(new File(filename)).useDelimiter("\\Z").next();
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }
        return EMAIL_ATTACHMENT;
    }

    static class HTMLDataSource implements DataSource
    {

        private String html;

        public HTMLDataSource(String htmlString) {
            html = htmlString;
        }

        @Override
        public InputStream getInputStream() throws IOException {
            if (html == null) throw new IOException("html message is null!");
            return new ByteArrayInputStream(html.getBytes());
        }

        @Override
        public OutputStream getOutputStream() throws IOException {
            throw new IOException("This DataHandler cannot write HTML");
        }

        @Override
        public String getContentType() {
            return "text/html";
        }

        @Override
        public String getName() {
            return "HTMLDataSource";
        }
    }
}