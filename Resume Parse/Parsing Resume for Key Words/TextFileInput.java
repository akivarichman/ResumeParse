// TextFileInput.java
// Copyright (c) 2000, 2005 Dorothy L. Nixon.  All rights reserved.
// package Java
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.IOException;

/**
 * Simplified buffered character input
 * stream from an input text file.
 * Manages an input text file,
 * handling all IOExceptions by generating
 * RuntimeExcpetions (run-time error
 * messages).
 *
 * If the text file cannot be created,
 * a RuntimeException is thrown,
 * which by default results an an
 * error message being printed to
 * the standard error stream.
 *
 * @author D. Nixon
 */
public class TextFileInput {

   /**  Name of text file  */
   private String filename;

   /**  Buffered character stream from file  */
   private BufferedReader br;  

   /**  Count of lines read so far.  */
   private int lineCount = 0;

   /**
    * Creates a buffered character input
    * strea, for the specified text file.
    *
    * @param filename the input text file.
    * @exception RuntimeException if an
    *          IOException is thrown when
    *          attempting to open the file.
    */
   public TextFileInput(String filename) {
      this.filename = filename;
      try {
         br = new BufferedReader(new InputStreamReader(new FileInputStream(filename)));
      } 
      catch ( IOException ioe ) {
         throw new RuntimeException(ioe);
      }  // catch
   }  // constructor

   /**
    * Closes this character input stream.
    * No more characters can be read from
    * this TextFileInput once it is closed.
    * @exception NullPointerException if
    *        the file is already closed.
    * @exception RuntimeException if an
    *       IOException is thrown when
    *       closing the file.
    */
   public void close() {
      try {
         br.close();
         br = null;
      } 
      catch ( NullPointerException npe ) {
         throw new NullPointerException(
                        filename + "already closed.");
      } 
      catch ( IOException ioe ) {
         throw new RuntimeException(ioe);
      }  // catch
   }  // method close

   /**
    * Reads a line of text from the file and
    * positions cursor at 0 for the next line.
    * Reads from the current cursor position
    * to end of line.
    * Implementation does not invoke read.
    *
    * @return the line of text, with
    *         end-of-line marker deleted.
    * @exception RuntimeException if an
    *          IOException is thrown when
    *          attempting to read from the file.
    */
   public String readLine() {
      try  {
         if ( br == null )
            throw new RuntimeException(
                               "Cannot read from closed file "
                               + filename + ".");
         String line = br.readLine();
         if ( line != null )
            lineCount++;
         return line;
      } catch (IOException ioe)  {
         throw new RuntimeException(ioe);
      }  // catch
   }  // method readLine()

   /**
    * Returns a count of lines
    * read from the file so far.
    */
   public int getLineCount() { 
      return lineCount;
   }

}