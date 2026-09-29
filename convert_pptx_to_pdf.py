import os
import sys
import win32com.client

def convert_pptx_to_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pptx_path = os.path.join(base_dir, "Smart_City_Management_Simulator_Presentation.pptx")
    pdf_path = os.path.join(base_dir, "Smart_City_Management_Simulator_Presentation.pdf")
    
    if not os.path.exists(pptx_path):
        print(f"Error: {pptx_path} not found")
        sys.exit(1)
        
    print(f"Converting: {pptx_path} -> {pdf_path}")
    
    ppt_app = win32com.client.Dispatch("PowerPoint.Application")
    # ppSaveAsPDF format constant is 32
    ppSaveAsPDF = 32
    
    try:
        presentation = ppt_app.Presentations.Open(pptx_path, WithWindow=False)
        presentation.SaveAs(pdf_path, ppSaveAsPDF)
        presentation.Close()
        print(f"Successfully created PDF at: {pdf_path}")
    except Exception as e:
        print(f"Conversion error: {e}")
        raise e
    finally:
        try:
            ppt_app.Quit()
        except:
            pass

if __name__ == "__main__":
    convert_pptx_to_pdf()
