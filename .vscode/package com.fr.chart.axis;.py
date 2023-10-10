package com.fr.chart.axis;
import com.fr.chart.chartattr.CategoryAxis;
import com.fr.chart.comp.BorderAttriPane;
import com.fr.chart.title.TextAttrRotationPane; 
import com.fr.design.gui.ilable.UILabel;	
import com.fr.design.layout.FRGUIPaneFactory;
import com.fr.design.layout.TableLayoutHelper;
import com.fr.general.Inter;
import com.fr.style.FormatBox;
import com.fr.utils.gui.GUICoreUtils;
import java.awt.Component;
import java.awt.FlowLayout;
import javax.swing.BorderFactory;
import javax.swing.JPanel;
public class CategoryAxisPane extends AxisStylePane<CategoryAxis>
{
  private static final long serialVersionUID = -2094545385428132997L;
  private BorderAttriPane borderAttriPane;
  private AxisArrowPane axisArrowPane;
  private DateAxisPane datePane;
  private TickMarkPane tickMarkPane;
  private AxisLabelPane axisLabelPane;
  private FormatBox formatBox;
  private TextAttrRotationPane textAttrPane;
  public CategoryAxisPane()
  {
    initComponents();
  }
  private void initComponents()
  {
    setLayout(FRGUIPaneFactory.createBorderLayout());
    JPanel localJPanel1 = FRGUIPaneFactory.createY_AXISBoxInnerContainer_S_Pane();
    add(localJPanel1, "North");
    JPanel localJPanel2 = FRGUIPaneFactory.createBorderLayout_L_Pane();
    localJPanel1.add(localJPanel2);
    JPanel localJPanel3 = FRGUIPaneFactory.createBorderLayout_L_Pane();
    localJPanel2.add(localJPanel3, "Center");
    localJPanel3.setBorder(BorderFactory.createEmptyBorder(0, 10, 0, 0));
    localJPanel2.setBorder(GUICoreUtils.createTitledBorder(Inter.getLocText("Axis-Style-Option")));
    JPanel localJPanel4 = FRGUIPaneFactory.createLeftFlowZeroGapBorderPane();
    this.borderAttriPane = new BorderAttriPane();
    localJPanel4.add(this.borderAttriPane);
    JPanel localJPanel5 = FRGUIPaneFactory.createLeftFlowZeroGapBorderPane();
    localJPanel5.add(this.axisArrowPane = new AxisArrowPane());
    this.datePane = new DateAxisPane();
    this.tickMarkPane = new TickMarkPane();
    this.axisLabelPane = new AxisLabelPane();
    JPanel localJPanel6 = FRGUIPaneFactory.createBorderLayout_S_Pane();
    localJPanel6.setBorder(BorderFactory.createEmptyBorder(6, 0, 0, 0));
    localJPanel6.add(new UILabel(Inter.getLocText(new String[] { "ChartF-Axis", "Style" }) + ":"), "North");
    Component[][] arrayOfComponent;1 = { { new UILabel(Inter.getLocText(new String[] { "Line", "Style" }) + ":"), localJPanel4 }, { new UILabel(Inter.getLocText(new String[] { "ChartF-Axis", "Set" }) + ":"), localJPanel5 }, { localJPanel6, this.datePane }, { new UILabel(Inter.getLocText("ChartF-Tick") + ":"), this.tickMarkPane }, { new UILabel(Inter.getLocText("Label") + ":"), this.axisLabelPane } };
    double[] arrayOfDouble1 = { -2.0D, -2.0D };
    double[] arrayOfDouble2 = { -2.0D, -2.0D, -2.0D, -2.0D, -2.0D, -2.0D };
    localJPanel3.add(TableLayoutHelper.createTableLayoutPane(arrayOfComponent;1, arrayOfDouble2, arrayOfDouble1));
    JPanel localJPanel7 = FRGUIPaneFactory.createLeftFlowZeroGapBorderPane();
    localJPanel7.setLayout(new FlowLayout(0, 35, 0));
    localJPanel7.add(this.formatBox = this.datePane.getFormatBox());
    Component[][] arrayOfComponent;2 = { { new UILabel(Inter.getLocText("StyleFormat-Category") + ":"), localJPanel7 } };
    JPanel localJPanel8 = FRGUIPaneFactory.createBorderLayout_S_Pane();
    localJPanel1.add(localJPanel8);
    JPanel localJPanel9 = FRGUIPaneFactory.createBorderLayout_S_Pane();
    localJPanel8.add(localJPanel9, "Center");
    localJPanel9.setBorder(BorderFactory.createEmptyBorder(0, 10, 0, 0));
    localJPanel8.setBorder(GUICoreUtils.createTitledBorder(Inter.getLocText("Number")));
    localJPanel9.add(TableLayoutHelper.createTableLayoutPane(arrayOfComponent;2, arrayOfDouble2, arrayOfDouble1), "Center");
    JPanel localJPanel10 = FRGUIPaneFactory.createBorderLayout_S_Pane();
    localJPanel1.add(localJPanel10);
    JPanel localJPanel11 = FRGUIPaneFactory.createBorderLayout_S_Pane();
    localJPanel10.add(localJPanel11, "Center");
    localJPanel11.setBorder(BorderFactory.createEmptyBorder(0, 10, 0, 0));
    localJPanel11.add(this.textAttrPane = new TextAttrRotationPane(), "Center");
    localJPanel10.setBorder(GUICoreUtils.createTitledBorder(Inter.getLocText(new String[] { "Label", "Style" })));
  }
  public void populate(CategoryAxis paramCategoryAxis)
  {
    if (paramCategoryAxis == null)
      return;
    this.tickMarkPane.populate(paramCategoryAxis);
    this.borderAttriPane.setLineColor(paramCategoryAxis.getAxisColor());
    this.borderAttriPane.setLineStyle(paramCategoryAxis.getAxisStyle());
    this.axisArrowPane.populate(paramCategoryAxis);
    this.axisLabelPane.populate(paramCategoryAxis);
    this.datePane.populate(paramCategoryAxis);
    this.formatBox.populate(paramCategoryAxis.getFormat());
    this.textAttrPane.populate(paramCategoryAxis.getTextAttr());
  }
  public void update(CategoryAxis paramCategoryAxis)
  {
    this.datePane.update(paramCategoryAxis);
    this.tickMarkPane.update(paramCategoryAxis);
    paramCategoryAxis.setAxisColor(this.borderAttriPane.getLineColor());
    paramCategoryAxis.setAxisStyle(this.borderAttriPane.getLineStyle());
    this.axisLabelPane.update(paramCategoryAxis);
    this.axisArrowPane.update(paramCategoryAxis);
    paramCategoryAxis.setFormat(this.formatBox.update());
    this.textAttrPane.update(paramCategoryAxis.getTextAttr());
  }
}
package com.fr.chart.axis;
import com.fr.base.NameObject;
import com.fr.chart.chartglyph.ChartAlertValue;
import com.fr.design.gui.controlpane.JControlPane;
import com.fr.design.gui.controlpane.NameObjectCreator;
import com.fr.design.gui.controlpane.NameableCreator;
import com.fr.general.Inter;
import com.fr.stable.Nameable;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
public class ChartAlertLinePane extends JControlPane
{
  public NameableCreator[] createNameableCreators()
  {
    return new NameableCreator[] { new NameObjectCreator(Inter.getLocText("ChartF-Alert-Line"), ChartAlertValue.class, ChartAlertValuePane.class) };
  }
  protected String title4PopupWindow()
  {
    return Inter.getLocText(new String[] { "Edit", "ChartF-Alert-Line" });
  }
  public void populate(ChartAlertValue[] paramArrayOfChartAlertValue)
  {
    if (paramArrayOfChartAlertValue == null)
      paramArrayOfChartAlertValue = new ChartAlertValue[0];
    ArrayList localArrayList = new ArrayList();
    for (int i = 0; i < paramArrayOfChartAlertValue.length; i++)
    {
      ChartAlertValue localChartAlertValue = paramArrayOfChartAlertValue[i];
      localArrayList.add(new NameObject(localChartAlertValue.getAlertPaneSelectName(), localChartAlertValue));
    }
    if (localArrayList.size() > 0)
      populate((Nameable[])localArrayList.toArray(new NameObject[localArrayList.size()]));
  }
  public ChartAlertValue[] updateAlertValues()
  {
    Nameable[] arrayOfNameable = update();
    NameObject[] arrayOfNameObject = new NameObject[arrayOfNameable.length];
    Arrays.asList(arrayOfNameable).toArray(arrayOfNameObject);
    if (arrayOfNameObject.length < 1)
      return new ChartAlertValue[0];
    ArrayList localArrayList = new ArrayList();
    for (int i = 0; i < arrayOfNameObject.length; i++)
    {
      NameObject localNameObject = arrayOfNameObject[i];
      ChartAlertValue localChartAlertValue = (ChartAlertValue)localNameObject.getObject();
      localChartAlertValue.setAlertPaneSelectName(localNameObject.getName());
      localArrayList.add(localChartAlertValue);
    }
    return (ChartAlertValue[])localArrayList.toArray(new ChartAlertValue[localArrayList.size()]);
  }
}package com.fr.chart.axis;
import com.fr.chart.chartattr.Axis;
import com.fr.chart.chartattr.Plot;
import com.fr.design.layout.FRGUIPaneFactory;
import com.fr.dialog.BasicPane;
import com.fr.general.Inter;
import java.awt.CardLayout;
import java.util.ArrayList;
import java.util.List;
import javax.swing.DefaultListModel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JSplitPane;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
public abstract class ChartStyleAxisPane extends BasicPane
  implements ListSelectionListener
{
  protected static final String CATE_AXIS = Inter.getLocText("ChartF-Category_Axis");
  protected static final String VALUE_AXIS = Inter.getLocText("Chart_F_Radar_Axis");
  protected static final String SECOND_AXIS = Inter.getLocText(new String[] { "Second", "Chart_F_Radar_Axis" });
  private JList mainList;
  private CardLayout cardLayout;
  private JPanel cardDisplayPane = null;
  private List<AxisStylePane> axisStylePaneList = new ArrayList();
  public ChartStyleAxisPane(Plot paramPlot)
  {
    initComponents(paramPlot);
  }
  private void initComponents(Plot paramPlot)
  {
    setLayout(FRGUIPaneFactory.createBorderLayout());
    DefaultListModel localDefaultListModel = new DefaultListModel();
    this.mainList = new JList(localDefaultListModel);
    AxisStyleObject[] arrayOfAxisStyleObject = createAxisStyleObjects(paramPlot);
    this.cardLayout = new CardLayout();
    this.cardDisplayPane = FRGUIPaneFactory.createCardLayout_S_Pane();
    this.cardDisplayPane.setLayout(this.cardLayout);
    for (int i = 0; i < arrayOfAxisStyleObject.length; i++)
    {
      AxisStyleObject localAxisStyleObject = arrayOfAxisStyleObject[i];
      localDefaultListModel.addElement(localAxisStyleObject.getName());
      AxisStylePane localAxisStylePane = localAxisStyleObject.getAxisStylePane();
      this.axisStylePaneList.add(localAxisStylePane);
      this.cardDisplayPane.add(localAxisStylePane, localAxisStyleObject.getName());
    }
    this.mainList.setSelectedIndex(0);
    this.mainList.addListSelectionListener(this);
    add(new JSplitPane(1, true, this.mainList, this.cardDisplayPane));
  }
  protected String title4PopupWindow()
  {
    return "Axis";
  }
  public void valueChanged(ListSelectionEvent paramListSelectionEvent)
  {
    this.cardLayout.show(this.cardDisplayPane, (String)this.mainList.getSelectedValue());
  }
  public abstract AxisStyleObject[] createAxisStyleObjects(Plot paramPlot);
  public void populate(Plot paramPlot)
  {
    int i = 0;
    int j = this.axisStylePaneList.size();
    while (i < j)
    {
      ((AxisStylePane)this.axisStylePaneList.get(i)).populate(getAxisFromPlotByListIndex(paramPlot, i));
      i++;
    }
  }
  public void update(Plot paramPlot)
  {
    int i = 0;
    int j = this.axisStylePaneList.size();
    while (i < j)
    {
      ((AxisStylePane)this.axisStylePaneList.get(i)).update(getAxisFromPlotByListIndex(paramPlot, i));
      i++;
    }
  }
  private Axis getAxisFromPlotByListIndex(Plot paramPlot, int paramInt)
  {
    return paramPlot.getAxis(paramInt);
  }
}package com.fr.chart.axis;
import com.fr.base.Formula;
import com.fr.chart.chartattr.CategoryAxis;
import com.fr.design.formula.FormulaPane;
import com.fr.design.gui.icheckbox.UICheckBox;
import com.fr.design.gui.icombobox.UIComboBox;
import com.fr.design.gui.ilable.UILabel;
import com.fr.design.gui.itextfield.UITextField;
import com.fr.design.layout.FRGUIPaneFactory;
import com.fr.design.layout.TableLayoutHelper;
import com.fr.dialog.BasicDialog;
import com.fr.dialog.DialogActionAdapter;
import com.fr.general.Inter;
import com.fr.stable.StringUtils;
import com.fr.style.FormatBox;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.HashMap;
import java.util.Map;
import javax.swing.BorderFactory;
import javax.swing.ButtonGroup;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.SwingUtilities;
public class DateAxisPane extends JPanel
{
  private static final long serialVersionUID = -9141181652050784467L;
  private static String[] TYPES = { Inter.getLocText("Year"), Inter.getLocText("Month"), Inter.getLocText("Sun"), Inter.getLocText("Sche-Hour"), Inter.getLocText("Sche-Minute"), Inter.getLocText("Sche-Second") };
  private static Map<String, Integer> VALUES = new HashMap();
  private static Map<Integer, String> INTS;
  private UICheckBox maxCheckBox;
  private UITextField maxValueField;
  private UICheckBox minCheckBox;
  private UITextField minValueField;
  private UICheckBox mainTickBox;
  private UITextField mainUnitField;
  private UIComboBox mainType;
  private UICheckBox secTickBox;
  private UITextField secUnitField;
  private UIComboBox secType;
  private JRadioButton isDateAxisButton;
  private JRadioButton isTextAxisButton;
  private JPanel tablePane;
  private FormatBox formatBox;
  private ActionListener bgListener = new ActionListener()
  {
    public void actionPerformed(ActionEvent paramAnonymousActionEvent)
    {
      DateAxisPane.this.checkVisible();
    }
  };
  public FormatBox getFormatBox()
  {
    return this.formatBox;
  }
  public DateAxisPane()
  {
    initComponents();
  }
  private void initComponents()
  {
    setLayout(FRGUIPaneFactory.createBorderLayout());
    this.formatBox = new FormatBox();
    JPanel localJPanel1 = FRGUIPaneFactory.createY_AXISBoxInnerContainer_S_Pane();
    add(localJPanel1, "North");
    this.isDateAxisButton = new JRadioButton(Inter.getLocText("Chart_Date_Axis"));
    this.isTextAxisButton = new JRadioButton(Inter.getLocText("Chart_Text_Axis"));
    this.isDateAxisButton.addActionListener(this.bgListener);
    this.isTextAxisButton.addActionListener(this.bgListener);
    ButtonGroup localButtonGroup = new ButtonGroup();
    localButtonGroup.add(this.isDateAxisButton);
    localButtonGroup.add(this.isTextAxisButton);
    JPanel localJPanel2 = TableLayoutHelper.createTableLayoutPane(new Component[][] { { this.isTextAxisButton, this.isDateAxisButton } }, new double[] { -1.0D }, new double[] { 0.3D, 0.3D });
    localJPanel1.add(localJPanel2);
    localJPanel2.setBorder(BorderFactory.createEmptyBorder(4, 2, 0, 0));
    this.minCheckBox = new UICheckBox(Inter.getLocText(new String[] { "Custom", "Min_Value" }));
    this.minValueField = new UITextField();
    this.minValueField.setEnabled(false);
    this.minValueField.setPreferredSize(new Dimension(100, 20));
    this.minCheckBox.addActionListener(new ActionListener()
    {
      public void actionPerformed(ActionEvent paramAnonymousActionEvent)
      {
        if (DateAxisPane.this.minCheckBox.isSelected())
          DateAxisPane.this.minValueField.setEditable(true);
        else
          DateAxisPane.this.minValueField.setEditable(false);
      }
    });
    addListener(this.minCheckBox, this.minValueField);
    this.maxCheckBox = new UICheckBox(Inter.getLocText(new String[] { "Custom", "Max_Value" }));
    this.maxValueField = new UITextField();
    this.maxValueField.setEnabled(false);
    this.maxValueField.setPreferredSize(new Dimension(100, 20));
    this.maxCheckBox.addActionListener(new ActionListener()
    {
      public void actionPerformed(ActionEvent paramAnonymousActionEvent)
      {
        if (DateAxisPane.this.maxCheckBox.isSelected())
          DateAxisPane.this.maxValueField.setEditable(true);
        else
          DateAxisPane.this.maxValueField.setEditable(false);
      }
    });
    addListener(this.maxCheckBox, this.maxValueField);
    this.mainTickBox = new UICheckBox(Inter.getLocText("MainGraduationUnit"));
    this.mainUnitField = new UITextField();
    this.mainUnitField.setPreferredSize(new Dimension(100, 20));
    this.mainUnitField.setEditable(false);
    this.mainType = new UIComboBox(TYPES);
    this.mainType.setEnabled(false);
    this.mainTickBox.addActionListener(new ActionListener()
    {
      public void actionPerformed(ActionEvent paramAnonymousActionEvent)
      {
        DateAxisPane.this.mainUnitField.setEditable(DateAxisPane.this.mainTickBox.isSelected());
        DateAxisPane.this.mainType.setEnabled(DateAxisPane.this.mainTickBox.isSelected());
      }
    });
    addListener(this.mainTickBox, this.mainUnitField);
    this.secTickBox = new UICheckBox(Inter.getLocText("SecondGraduationUnit"));
    this.secUnitField = new UITextField();
    this.secUnitField.setPreferredSize(new Dimension(100, 20));
    this.secUnitField.setEditable(false);
    this.secType = new UIComboBox(TYPES);
    this.secType.setEnabled(false);
    this.secTickBox.addActionListener(new ActionListener()
    {
      public void actionPerformed(ActionEvent paramAnonymousActionEvent)
      {
        DateAxisPane.this.secUnitField.setEditable(DateAxisPane.this.secTickBox.isSelected());
        DateAxisPane.this.secType.setEnabled(DateAxisPane.this.secTickBox.isSelected());
      }
    });
    addListener(this.secTickBox, this.secUnitField);
    double d = -1.0D;
    double[] arrayOfDouble1 = { d, d, d, d };
    double[] arrayOfDouble2 = { 0.3D, 0.2D, 0.25D };
    Component[][] arrayOfComponent; = { { this.minCheckBox, this.minValueField, new UILabel(Inter.getLocText("StyleFormat-Sample") + ": 2007-01-01") }, { this.maxCheckBox, this.maxValueField, new UILabel(Inter.getLocText("StyleFormat-Sample") + ": 2009-01-01") }, { this.mainTickBox, this.mainUnitField, this.mainType }, { this.secTickBox, this.secUnitField, this.secType } };
    this.tablePane = TableLayoutHelper.createTableLayoutPane(arrayOfComponent;, arrayOfDouble1, arrayOfDouble2);
    localJPanel1.add(this.tablePane);
    checkVisible();
  }
  private void addListener(final UICheckBox paramUICheckBox, final UITextField paramUITextField)
  {
    paramUITextField.addMouseListener(new MouseAdapter()
    {
      public void mousePressed(MouseEvent paramAnonymousMouseEvent)
      {
        if (paramUICheckBox.isSelected())
          DateAxisPane.this.showFormulaPane(paramUITextField);
      }
    });
    paramUITextField.addKeyListener(new KeyAdapter()
    {
      public void keyTyped(KeyEvent paramAnonymousKeyEvent)
      {
        if (paramUICheckBox.isSelected())
        {
          paramAnonymousKeyEvent.consume();
          DateAxisPane.this.showFormulaPane(paramUITextField);
        }
      }
    });
  }
  private void showFormulaPane(final UITextField paramUITextField)
  {
    final FormulaPane localFormulaPane = new FormulaPane();
    localFormulaPane.populate(new Formula(paramUITextField.getText()));
    BasicDialog localBasicDialog = localFormulaPane.showLargeWindow(SwingUtilities.getWindowAncestor(this), new DialogActionAdapter()
    {
      public void doOk()
      {
        Formula localFormula = localFormulaPane.update();
        paramUITextField.setText(localFormula.toString());
      }
    });
    localBasicDialog.setVisible(true);
  }
  private void checkVisible()
  {
    if (this.isDateAxisButton.isSelected())
    {
      this.tablePane.setVisible(true);
      this.formatBox.setDateTypeBox();
    }
    else
    {
      this.tablePane.setVisible(false);
      this.formatBox.setTextTypeBox();
    }
  }
  private void populateMain(CategoryAxis paramCategoryAxis)
  {
    if ((paramCategoryAxis.isCustomMainUnit()) &&(paramCategoryAxis.getMainUnit() != null))
    {
      this.mainTickBox.setSelected(true);
      this.mainUnitField.setText(paramCategoryAxis.getMainUnit().toString());
      this.mainUnitField.setEditable(true);
      this.mainType.setEditable(true);
      this.mainType.setEnabled(true);
      this.mainType.setSelectedItem(INTS.get(Integer.valueOf(paramCategoryAxis.getMainType())));
    }
    else
    {
      this.mainUnitField.setEditable(false);
      this.mainType.setEditable(false);
      this.mainType.setEnabled(false);
    }
  }
  private void populateSecond(CategoryAxis paramCategoryAxis)
  {
    if ((paramCategoryAxis.isCustomSecUnit()) && (paramCategoryAxis.getSecUnit() != null))
    {
      this.secTickBox.setSelected(true);
      this.secUnitField.setText(paramCategoryAxis.getSecUnit().toString());
      this.secUnitField.setEditable(true);
      this.secType.setEditable(true);
      this.secType.setEnabled(true);
      this.secType.setSelectedItem(INTS.get(Integer.valueOf(paramCategoryAxis.getSecondType())));
    }
    else
    {
      this.secUnitField.setEditable(false);
      this.secType.setEditable(false);
      this.secType.setEnabled(false);
    }
  }
  private void updateMain(CategoryAxis paramCategoryAxis)
  {
    if ((this.mainTickBox.isSelected()) && (StringUtils.isNotEmpty(this.mainUnitField.getText())))
    {
      paramCategoryAxis.setCustomMainUnit(true);
      paramCategoryAxis.setMainUnit(new Formula(this.mainUnitField.getText()));
      paramCategoryAxis.setMainType(((Integer)VALUES.get(this.mainType.getSelectedItem())).intValue());
    }
    else
    {
      paramCategoryAxis.setCustomMainUnit(false);
    }
  }
  private void updateSecond(CategoryAxis paramCategoryAxis)
  {
    if ((this.secTickBox.isSelected()) &&(StringUtils.isNotEmpty(this.secUnitField.getText())))
    {
      paramCategoryAxis.setCustomSecUnit(true);
      paramCategoryAxis.setSecUnit(new Formula(this.secUnitField.getText()));
      paramCategoryAxis.setSecondType(((Integer)VALUES.get(this.secType.getSelectedItem())).intValue());
    }
    else
    {
      paramCategoryAxis.setCustomSecUnit(false);
    }
  }
  public void populate(CategoryAxis paramCategoryAxis)
  {
    if (paramCategoryAxis == null)
      return;
    if (!paramCategoryAxis.isDate())
    {
      this.isTextAxisButton.setSelected(true);
      return;
    }
    this.isDateAxisButton.setSelected(true);
    this.tablePane.setVisible(true);
    if ((paramCategoryAxis.isCustomMinValue()) &&(paramCategoryAxis.getMinValue() != null))
    {
      this.minCheckBox.setSelected(true);
      this.minValueField.setText(paramCategoryAxis.getMinValue().toString());
      this.minValueField.setEnabled(true);
      this.minValueField.setEditable(true);
    }
    else
    {
      this.minValueField.setEnabled(false);
      this.minValueField.setEditable(false);
    }
    if ((paramCategoryAxis.isCustomMaxValue()) &&(paramCategoryAxis.getMaxValue() != null))
    {
      this.maxCheckBox.setSelected(true);
      this.maxValueField.setText(paramCategoryAxis.getMaxValue().toString());
      this.maxValueField.setEnabled(true);
      this.maxValueField.setEditable(true);
    }
    else
    {
      this.maxValueField.setEnabled(false);
      this.maxValueField.setEditable(false);
    }
    populateMain(paramCategoryAxis);
    populateSecond(paramCategoryAxis);
  }
  public void update(CategoryAxis paramCategoryAxis)
  {
    if (this.isTextAxisButton.isSelected())
    {
      paramCategoryAxis.setDate(false);
      return;
    }
    paramCategoryAxis.setDate(true);
    updateMain(paramCategoryAxis);
    updateSecond(paramCategoryAxis);
    if (this.minCheckBox.isSelected())
    {
      paramCategoryAxis.setCustomMinValue(!StringUtils.isEmpty(this.minValueField.getText()));
      paramCategoryAxis.setMinValue(new Formula(this.minValueField.getText()));
    }
    else
    {
      paramCategoryAxis.setCustomMinValue(false);
    }
    if (this.maxCheckBox.isSelected())
    {
      paramCategoryAxis.setCustomMaxValue(!StringUtils.isEmpty(this.maxValueField.getText()));
      paramCategoryAxis.setMaxValue(new Formula(this.maxValueField.getText()));
    }
    else
    {
      paramCategoryAxis.setCustomMaxValue(false);
    }
  }
  static
  {
    VALUES.put(Inter.getLocText("Year"), Integer.valueOf(3));
    VALUES.put(Inter.getLocText("Month"), Integer.valueOf(2));
    VALUES.put(Inter.getLocText("Sun"), Integer.valueOf(1));
    VALUES.put(Inter.getLocText("Sche-Hour"), Integer.valueOf(4));
    VALUES.put(Inter.getLocText("Sche-Minute"), Integer.valueOf(5));
    VALUES.put(Inter.getLocText("Sche-Second"), Integer.valueOf(6));
    INTS = new HashMap();
    INTS.put(Integer.valueOf(3), Inter.getLocText("Year"));
    INTS.put(Integer.valueOf(2), Inter.getLocText("Month"));
    INTS.put(Integer.valueOf(1), Inter.getLocText("Sun"));
    INTS.put(Integer.valueOf(4), Inter.getLocText("Sche-Hour"));
    INTS.put(Integer.valueOf(5), Inter.getLocText("Sche-Minute"));
    INTS.put(Integer.valueOf(6), Inter.getLocText("Sche-Second"));
  }
}
package com.fr.chart.axis;
import com.fr.chart.chartattr.Axis;
import com.fr.chart.comp.BorderAttriPane;
import com.fr.design.layout.FRGUIPaneFactory;
import com.fr.dialog.BasicPane;
import com.fr.general.Inter;
import java.awt.CardLayout;
import javax.swing.DefaultListModel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JSplitPane;
public class GridStylePane extends BasicPane
{
  private static final long serialVersionUID = 1L;
  private BorderAttriPane borderAttriPane;
  private CardLayout cardLayout = null;
  private JList mainList = null;
  private JPanel cardDisplayPane = null;
  private String[] listName = { Inter.getLocText(new String[] { "Line", "Style" }) };
  public GridStylePane()
  {
    inits();
  }
  public void inits()
  {
    setLayout(FRGUIPaneFactory.createBorderLayout());
    DefaultListModel localDefaultListModel = new DefaultListModel();
    this.mainList = new JList(localDefaultListModel);
    for (int i = 0; i < this.listName.length; i++)
      localDefaultListModel.addElement(this.listName[i]);
    this.cardLayout = new CardLayout();
    this.cardDisplayPane = FRGUIPaneFactory.createCardLayout_S_Pane();
    this.cardDisplayPane.setLayout(this.cardLayout);
    this.borderAttriPane = new BorderAttriPane();
    this.cardDisplayPane.add(this.borderAttriPane, this.listName[0]);
    this.mainList.setSelectedIndex(0);
    add(new JSplitPane(1, true, this.mainList, this.cardDisplayPane));
  }
  protected String title4PopupWindow()
  {
    return Inter.getLocText("Chart-SetMainGridStyle");
  }
  public void populate(Axis paramAxis, boolean paramBoolean)
  {
    if (paramBoolean)
    {
      this.borderAttriPane.setLineColor(paramAxis.getMainGridColor());
      this.borderAttriPane.setLineStyle(paramAxis.getMainGridStyle());
    }
  }
  public void update(Axis paramAxis, boolean paramBoolean)
  {
    if (paramBoolean)
    {
      paramAxis.setMainGridColor(this.borderAttriPane.getLineColor());
      paramAxis.setMainGridStyle(this.borderAttriPane.getLineStyle());
    }
  }
}
package com.fr.chart.chartData.reportData;
import com.fr.chart.chartdata.MapMoreLayerReportDefinition;
import com.fr.chart.chartdata.MapMoreLayerTableDefinition;
import com.fr.chart.chartdata.TopDefinition;
import com.fr.design.beans.FurtherBasicBeanPane;
import com.fr.design.gui.frpane.UIComboBoxPane;
import com.fr.design.gui.xlabel.BoldFontTextLabel;
import com.fr.general.Inter;
import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.util.ArrayList;
import java.util.List;
import javax.swing.JPanel;
public class MapCubeDataPane extends UIComboBoxPane<TopDefinition>
{
  private MapReportCubeDataPane reportPane;
  private MapTableCubeDataPane tablePane;
  protected void initLayout()
  {
    setLayout(new BorderLayout(0, 0));
    JPanel localJPanel = new JPanel(new FlowLayout(0, 0, 0));
    localJPanel.add(new BoldFontTextLabel(Inter.getLocText("ChartF-Data-Resource") + ":"));
    localJPanel.add(this.jcb);
    add(localJPanel, "North");
    add(this.cardPane, "Center");
  }
  public void setEditingLayerCount(int paramInt)
  {
    if (this.reportPane != null)
      this.reportPane.setEditingLayer(paramInt);
    if (this.tablePane != null)
      this.tablePane.setEditingLayer(paramInt);
  }
  protected List<FurtherBasicBeanPane<? extends TopDefinition>> initPaneList()
  {
    ArrayList localArrayList = new ArrayList();
    localArrayList.add(this.tablePane = new MapTableCubeDataPane());
    localArrayList.add(this.reportPane = new MapReportCubeDataPane());
    return localArrayList;
  }
  protected String title4PopupWindow()
  {
    return Inter.getLocText("LayerData");
  }
  public void populateBean(TopDefinition paramTopDefinition)
  {
    Object localObject;
    if ((paramTopDefinition instanceof MapMoreLayerReportDefinition))
    {
      setSelectedIndex(1);
      localObject = (MapMoreLayerReportDefinition)paramTopDefinition;
      this.reportPane.populateBean((MapMoreLayerReportDefinition)localObject);
    }
    else if ((paramTopDefinition instanceof MapMoreLayerTableDefinition))
    {
      localObject = (MapMoreLayerTableDefinition)paramTopDefinition;
      setSelectedIndex(0);
      this.tablePane.populateBean((MapMoreLayerTableDefinition)localObject);
    }
  }
  public TopDefinition update()
  {
    if (getSelectedIndex() == 0)
      return this.tablePane.updateBean();
    return this.reportPane.updateBean();
  }
}
package com.fr.chart.chartData.reportData;
import com.fr.base.MapXMLHelper;
import com.fr.chart.chartglyph.MapAttr;
import com.fr.design.DesignerEnvManager;
import com.fr.design.beans.BasicBeanPane;
import com.fr.dialog.BasicDialog;
import com.fr.dialog.DialogActionAdapter;
import com.fr.general.FRLogger;
import com.fr.general.Inter;
import com.fr.utils.gui.GUICoreUtils;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Point;
import java.awt.Window;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import javax.swing.JScrollPane;
import javax.swing.JTree;
import javax.swing.SwingUtilities;
import javax.swing.SwingWorker;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeModel;
import javax.swing.tree.TreePath;
public class MapCubeLayerPane extends BasicBeanPane<String>
{
  private JTree mapTree;
  private DefaultMutableTreeNode root;
  private String editingMap = "";
  private List<ChangeListener> fireWhenTreeChange = new ArrayList();
  private List<String> hasDealNames = new ArrayList();
  MouseListener mapListener = new MouseAdapter()
  {
    public void mouseClicked(MouseEvent paramAnonymousMouseEvent)
    {
      TreePath localTreePath = MapCubeLayerPane.this.mapTree.getSelectionPath();
      if (localTreePath == null)
        return;
      String str = ((DefaultMutableTreeNode)localTreePath.getLastPathComponent()).getUserObject().toString();
      if (SwingUtilities.isRightMouseButton(paramAnonymousMouseEvent))
      {
        final MapAttr localMapAttr1 = (MapAttr)MapXMLHelper.getInstance().getMapAttr(MapCubeLayerPane.this.editingMap);
        final MapCubeSetDataPane localMapCubeSetDataPane = new MapCubeSetDataPane();
        localMapCubeSetDataPane.freshComboxNames();
        MapAttr localMapAttr2 = (MapAttr)MapXMLHelper.getInstance().getMapAttr(str);
        if (localMapAttr2 != null)
        {
          ArrayList localArrayList = new ArrayList();
          Iterator localIterator = localMapAttr2.shapeValuesIterator();
          while (localIterator.hasNext())
          {
            localObject = localIterator.next();
            localArrayList.add(new Object[] { localObject, localMapAttr1.getLayerTo(localObject.toString()) });
          }
          localMapCubeSetDataPane.populateBean(localArrayList);
        }
        int i = (int)(MapCubeLayerPane.this.mapTree.getLocationOnScreen().getX() + MapCubeLayerPane.this.mapTree.getWidth());
        int j = (int)paramAnonymousMouseEvent.getLocationOnScreen().getY();
        Object localObject = localMapCubeSetDataPane.showWindow(SwingUtilities.getWindowAncestor(localMapCubeSetDataPane), new DialogActionAdapter()
        {
          public void doOk()
          {
            List localList = localMapCubeSetDataPane.updateBean();
            for (int i = 0; i < localList.size(); i++)
            {
              Object[] arrayOfObject = (Object[])localList.get(i);
              localMapAttr1.putLayerTo(arrayOfObject[0], arrayOfObject[1]);
            }
MapCubeLayerPane.this.initRootTree(MapCubeLayerPane.this.editingMap);
            MapCubeLayerPane.this.saveMapInfo();
          }
        });
        ((BasicDialog)localObject).setBasicDialogSize(300, 300);
        GUICoreUtils.centerWindow((Window)localObject);
        ((BasicDialog)localObject).setVisible(true);
      }
    }
  };
  public MapCubeLayerPane()
  {
    initCom();
  }
  private void initCom()
  {
    setLayout(new BorderLayout());
    this.root = new DefaultMutableTreeNode();
    this.mapTree = new JTree(this.root);
    this.mapTree.setRootVisible(false);
    this.mapTree.addMouseListener(this.mapListener);
    JScrollPane localJScrollPane = new JScrollPane(this.mapTree);
    localJScrollPane.setPreferredSize(new Dimension(100, 100));
    add(localJScrollPane, "Center");
  }
  public int getTreeDepth()
  {
    return this.root.getDepth();
  }
  public void initRootTree(String paramString)
  {
    this.editingMap = paramString;
    this.root.removeAllChildren();
    DefaultMutableTreeNode localDefaultMutableTreeNode = new DefaultMutableTreeNode(paramString);
    this.root.add(localDefaultMutableTreeNode);
    MapAttr localMapAttr = (MapAttr)MapXMLHelper.getInstance().getMapAttr(paramString);
    this.hasDealNames.clear();
    add4Node(localMapAttr, localDefaultMutableTreeNode, paramString);
    this.mapTree.doLayout();
    this.mapTree.validate();
    ((DefaultTreeModel)this.mapTree.getModel()).reload();
    for (int i = 0; i < this.fireWhenTreeChange.size(); i++)
      ((ChangeListener)this.fireWhenTreeChange.get(i)).stateChanged(new ChangeEvent(this));
  }
  public void addChangeListener(ChangeListener paramChangeListener)
  {
    this.fireWhenTreeChange.add(paramChangeListener);
  }
  private void add4Node(MapAttr paramMapAttr, DefaultMutableTreeNode paramDefaultMutableTreeNode, String paramString)
  {
    MapAttr localMapAttr1 = (MapAttr)MapXMLHelper.getInstance().getMapAttr(paramString);
    if (localMapAttr1 != null)
    {
      Iterator localIterator = localMapAttr1.shapeValuesIterator();
      while (localIterator.hasNext())
      {
        Object localObject = localIterator.next();
        String str = paramMapAttr.getLayerTo(localObject.toString()).toString();
        MapAttr localMapAttr2 = (MapAttr)MapXMLHelper.getInstance().getMapAttr(str);
        if (localMapAttr2 != null)
        {
          DefaultMutableTreeNode localDefaultMutableTreeNode = new DefaultMutableTreeNode(localObject);
          paramDefaultMutableTreeNode.add(localDefaultMutableTreeNode);
          if (!this.hasDealNames.contains(localDefaultMutableTreeNode.getUserObject().toString()))
          {
this.hasDealNames.add(localDefaultMutableTreeNode.getUserObject().toString());
            add4Node(paramMapAttr, localDefaultMutableTreeNode, str);
          }
        }
      }
    }
  }
  private void saveMapInfo()
  {
    SwingWorker local2 = new SwingWorker()
    {
      protected Integer doInBackground()
        throws Exception
      {
        MapXMLHelper.getInstance().writerMapSourceWhenEditMap();
        return Integer.valueOf(0);
      }
      protected void done()
      {
        FRLogger.getLogger().info("Map Save End");
      }
    };
    local2.execute();
    DesignerEnvManager.addWorkers(local2);
  }
  public void populateBean(String paramString)
  {
    initRootTree(paramString);
  }
  public void updateBean(String paramString)
  {
  }
  public String updateBean()
  {
    return "";
  }
  protected String title4PopupWindow()
  {
    return Inter.getLocText("LayerGrade");
  }
}
package com.fr.chart.chartData.reportData;
import com.fr.base.MapXMLHelper;
import com.fr.design.beans.BasicBeanPane;
import com.fr.design.gui.itableeditorpane.UIArrayTableModel;
import com.fr.design.gui.itableeditorpane.UITableEditorPane;
import com.fr.editor.ValueEditorPane;
import com.fr.editor.ValueEditorPaneFactory;
import com.fr.editor.gui.ComboBoxUseEditor;
import com.fr.editor.gui.Editor;
import com.fr.editor.gui.TextEditor;
import com.fr.general.Inter;
import java.awt.BorderLayout;
import java.awt.Component;
import java.util.List;
import javax.swing.AbstractCellEditor;
import javax.swing.JTable;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.TableCellEditor;
public class MapCubeSetDataPane extends BasicBeanPane<List>
{
  private UITableEditorPane tableEditorPane;
  private String[] initNames = { "" };
  public MapCubeSetDataPane()
  {
    initCom();
  }
  private void initCom()
  {
    setLayout(new BorderLayout(0, 0));
    UIArrayTableModel local1 = new UIArrayTableModel(new String[] { Inter.getLocText("Area_Name"), Inter.getLocText("Layer_Corresponding_Map") }, new int[0])
    {
      public boolean isCellEditable(int paramAnonymousInt1, int paramAnonymousInt2)
      {
        return paramAnonymousInt2 != 0;
      }
    };
    local1.setDefaultEditor(Object.class, new DefaultComboBoxEditor());
    local1.setDefaultRenderer(Object.class, new DefaultComboBoxRenderer());
    this.tableEditorPane = new UITableEditorPane(local1);
    add(this.tableEditorPane);
    local1.addRow(new Object[] { "", "" });
  }
  public void freshComboxNames()
  {
    this.initNames = MapXMLHelper.getInstance().mapAllNames();
  }
  public void populateBean(List paramList)
  {
    this.tableEditorPane.populate(paramList.toArray());
  }
  public List updateBean()
  {
    return this.tableEditorPane.update();
  }
  protected String title4PopupWindow()
  {
    return Inter.getLocText("Lower_LayerSet");
  }
  private class DefaultComboBoxRenderer extends DefaultTableCellRenderer
  {
    private static final long serialVersionUID = -695450455731718014L;
    private ValueEditorPane cellEditor = ValueEditorPaneFactory.createValueEditorPane(new Editor[] { new ComboBoxUseEditor(MapCubeSetDataPane.this.initNames) });
    public DefaultComboBoxRenderer()
    {
    }
    public Component getTableCellRendererComponent(JTable paramJTable, Object paramObject, boolean paramBoolean1, boolean paramBoolean2, int paramInt1, int paramInt2)
    {
      if (paramInt2 == 0)
        this.cellEditor = ValueEditorPaneFactory.createValueEditorPane(new Editor[] { new TextEditor() });
      else
        this.cellEditor = ValueEditorPaneFactory.createValueEditorPane(new Editor[] { new ComboBoxUseEditor(MapCubeSetDataPane.this.initNames) });
      this.cellEditor.populate(paramObject == null ? "" : paramObject);
      return this.cellEditor;
    }
  }
  private class DefaultComboBoxEditor extends AbstractCellEditor
    implements TableCellEditor
  {
    private static final long serialVersionUID = -3239789564820528730L;
    private ValueEditorPane cellEditor = ValueEditorPaneFactory.createValueEditorPane(new Editor[] { new ComboBoxUseEditor(MapCubeSetDataPane.this.initNames) });
    public DefaultComboBoxEditor()
    {
    }
    public Component getTableCellEditorComponent(JTable paramJTable, Object paramObject, boolean paramBoolean, int paramInt1, int paramInt2)
    {
      if (paramInt2 == 0)
        this.cellEditor = ValueEditorPaneFactory.createValueEditorPane(new Editor[] { new TextEditor() });
      else
        this.cellEditor = ValueEditorPaneFactory.createValueEditorPane(new Editor[] { new ComboBoxUseEditor(MapCubeSetDataPane.this.initNames) });
      this.cellEditor.populate(paramObject == null ? "" : paramObject);
      return this.cellEditor;
    }
    public Object getCellEditorValue()
    {
      return this.cellEditor.update();
    }
  }
}package com.fr.chart.chartData.reportData;
import com.fr.chart.chartattr.Chart;
import com.fr.chart.chartattr.ChartCollection;
import com.fr.chart.chartdata.MapMoreLayerReportDefinition;
import com.fr.chart.chartdata.MapMoreLayerTableDefinition;
import com.fr.chart.chartdata.MapSingleLayerReportDefinition;
import com.fr.chart.chartdata.MapSingleLayerTableDefinition;
import com.fr.chart.chartdata.TopDefinition;
import com.fr.design.beans.FurtherBasicBeanPane;
import com.fr.design.gui.frpane.AttributeChangeListener;
import com.fr.design.gui.frpane.UIComboBoxPane;
import com.fr.design.gui.xlabel.BoldFontTextLabel;
import com.fr.design.mainframe.chart.gui.data.DataContentsPane;
import com.fr.dialog.BasicScrollPane;
import com.fr.general.Inter;
import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.util.ArrayList;
import java.util.List;
import javax.swing.JPanel;
public class MapDataPane extends DataContentsPane
{
  private UIComboBoxPane<Chart> mainPane;
  private MapMoreCubeLayerPane morePane;
  private MapSinglePane singlePane;
  private AttributeChangeListener listener;
  public MapDataPane(AttributeChangeListener paramAttributeChangeListener)
  {
    this.listener = paramAttributeChangeListener;
  }
  public void populate(ChartCollection paramChartCollection)
  {
    TopDefinition localTopDefinition = paramChartCollection.getFilterDefinition();
    this.morePane.init4PopuMapTree(paramChartCollection);
    if ((localTopDefinition instanceof MapSingleLayerTableDefinition))
    {
      this.mainPane.setSelectedIndex(0);
      this.singlePane.populateBean(localTopDefinition);
    }
    else if ((localTopDefinition instanceof MapMoreLayerTableDefinition))
    {
      this.mainPane.setSelectedIndex(1);
      this.morePane.populateBean(paramChartCollection);
    }
    else if ((localTopDefinition instanceof MapMoreLayerReportDefinition))
    {
      this.mainPane.setSelectedIndex(1);
      this.morePane.populateBean(paramChartCollection);
    }
    else if ((localTopDefinition instanceof MapSingleLayerReportDefinition))
    {
      this.mainPane.setSelectedIndex(0);
      this.singlePane.populateBean(localTopDefinition);
    }
    initAllListeners();
    addAttributeChangeListener(this.listener);
  }
  public void update(ChartCollection paramChartCollection)
  {
    if (this.mainPane.getSelectedIndex() == 0)
      paramChartCollection.setFilterDefinition(this.singlePane.updateBean());
    else
      this.morePane.updateBean(paramChartCollection);
  }
  protected JPanel createContentPane()
  {
    BasicScrollPane local1 = new BasicScrollPane()
    {
      protected JPanel createContentPane()
      {
        JPanel localJPanel = new JPanel();
        localJPanel.setLayout(new BorderLayout());
        MapDataPane.this.mainPane = new UIComboBoxPane()
        {
          protected void initLayout()
          {
            setLayout(new BorderLayout(0, 6));
            JPanel localJPanel = new JPanel(new FlowLayout(0));
            localJPanel.add(new BoldFontTextLabel(Inter.getLocText("Map Show Type") + ":"));
            localJPanel.add(this.jcb);
            add(localJPanel, "North");
            add(this.cardPane, "Center");
          }
          protected List<FurtherBasicBeanPane<? extends Chart>> initPaneList()
          {
            ArrayList localArrayList = new ArrayList();
            localArrayList.add(MapDataPane.this.singlePane = new MapSinglePane());
            localArrayList.add(MapDataPane.this.morePane = new MapMoreCubeLayerPane());
            return localArrayList;
          }
          protected String title4PopupWindow()
          {
            return Inter.getLocText(new String[] { "Chart-Map", "Data" });
          }
        };
        localJPanel.add(MapDataPane.this.mainPane, "Center");
        return localJPanel;
      }
      public void populateBean(Chart paramAnonymousChart)
      {
      }
      protected String title4PopupWindow()
      {
        return null;
      }
    };
    return local1;
  }
  public String getIconPath()
  {
    return "com/fr/design/images/chart/ChartData.png";
  }
  public String title4PopupWindow()
  {
    return Inter.getLocText(new String[] { "Chart-Map", "Data" });
  }
  public void setSurpportCellData(boolean paramBoolean)
  {
    this.morePane.setSurpportCellData(paramBoolean);
    this.singlePane.setSurpportCellData(paramBoolean);
  }
}
package com.fr.chart.chartData.reportData;
import com.fr.chart.chartattr.Chart;
import com.fr.chart.chartattr.ChartCollection;
import com.fr.chart.chartattr.MapPlot;
import com.fr.dialog.BasicPane;
import com.fr.dialog.MultiTabPane;
import com.fr.general.Inter;
import java.util.ArrayList;
import java.util.List;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
public class MapMoreCubeLayerPane extends MultiTabPane<ChartCollection>
{
  private static final long serialVersionUID = -174286187746442527L;
  private MapCubeLayerPane layerPane;
  private MapCubeDataPane dataPane;
  protected List<BasicPane> initPaneList()
  {
    ArrayList localArrayList = new ArrayList();
    localArrayList.add(this.layerPane = new MapCubeLayerPane());
    localArrayList.add(this.dataPane = new MapCubeDataPane());
    this.layerPane.addChangeListener(new ChangeListener()
    {
      public void stateChanged(ChangeEvent paramAnonymousChangeEvent)
      {
        MapMoreCubeLayerPane.this.dataPane.setEditingLayerCount(MapMoreCubeLayerPane.this.layerPane.getTreeDepth());
      }
    });
    return localArrayList;
  }
  public ChartCollection updateBean()
  {
    return null;
  }
  public void populateBean(ChartCollection paramChartCollection)
  {
    Chart localChart = paramChartCollection.getSelectedChart();
    if ((localChart != null) && ((localChart.getPlot() instanceof MapPlot)))
    {
      MapPlot localMapPlot = (MapPlot)localChart.getPlot();
      this.layerPane.populateBean(localMapPlot.getMapName());
    }
    this.dataPane.populateBean(paramChartCollection.getFilterDefinition());
  }
  public void updateBean(ChartCollection paramChartCollection)
  {
    paramChartCollection.setFilterDefinition(this.dataPane.update());
    Chart localChart = paramChartCollection.getSelectedChart();
    if ((localChart != null) && ((localChart.getPlot() instanceof MapPlot)))
    {
      MapPlot localMapPlot = (MapPlot)localChart.getPlot();
      this.layerPane.updateBean(localMapPlot.getMapName());
    }
  }
  public void init4PopuMapTree(ChartCollection paramChartCollection)
  {
    Chart localChart = paramChartCollection.getSelectedChart();
    if ((localChart != null) && ((localChart.getPlot() instanceof MapPlot)))
    {
      MapPlot localMapPlot = (MapPlot)localChart.getPlot();
      if (this.layerPane != null)
        this.layerPane.initRootTree(localMapPlot.getMapName());
      if (this.dataPane != null)
        this.dataPane.setEditingLayerCount(this.layerPane == null ? 1 : this.layerPane.getTreeDepth());
    }
  }
  public boolean accept(Object paramObject)
  {
    return true;
  }
  public String title4PopupWindow()
  {
    return Inter.getLocText("Muiti_In");
  }
  public void reset()
  {
  }
  public void setSurpportCellData(boolean paramBoolean)
  {
    this.dataPane.justSupportOneSelect(paramBoolean);
  }
}package com.fr.chart.chartData.reportData;
import com.fr.base.Formula;
import com.fr.chart.chartdata.MapSingleLayerReportDefinition;
import com.fr.chart.chartdata.SeriesDefinition;
import com.fr.constants.FRSwingConstants;
import com.fr.design.beans.BasicBeanPane;
import com.fr.design.formula.TinyFormulaPane;
import com.fr.design.gui.frpane.UICorrelationPane;
import com.fr.design.gui.ilable.UILabel;
import com.fr.design.gui.itable.UITableEditor;
import com.fr.design.gui.itextfield.UITextField;
import com.fr.general.Inter;
import java.awt.BorderLayout;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;
import java.util.ArrayList;
import java.util.List;
import javax.swing.JComponent;
import javax.swing.JPanel;
import javax.swing.JTable;
import javax.swing.table.TableModel;
public class MapMoreReportIndexPane extends BasicBeanPane<MapSingleLayerReportDefinition>
{
  private String title = "";
  private TinyFormulaPane areaNamePane;
  private UICorrelationPane tabPane;
  public MapMoreReportIndexPane()
  {
    initPane();
  }
  public MapMoreReportIndexPane(String paramString)
  {
    this.title = paramString;
    initPane();
  }
  private void initPane()
  {
    setLayout(new BorderLayout(0, 0));
    JPanel localJPanel = new JPanel();
    add(localJPanel, "North");
    localJPanel.setLayout(new FlowLayout(0));
    localJPanel.add(new UILabel(Inter.getLocText("Area_Name") + ":"));
    this.areaNamePane = new TinyFormulaPane();
    this.areaNamePane.setPreferredSize(new Dimension(120, 20));
    localJPanel.add(this.areaNamePane);
    this.tabPane = new UICorrelationPane(new String[] { Inter.getLocLongText("Filed", "Title"), Inter.getLocText("Area_Value") })
    {
      public UITableEditor createUITableEditor()
      {
        return new MapMoreReportIndexPane.InnerTableEditor(MapMoreReportIndexPane.this, null);
      }
    };
    add(this.tabPane, "Center");
  }
  public void populateBean(MapSingleLayerReportDefinition paramMapSingleLayerReportDefinition)
  {
    if ((paramMapSingleLayerReportDefinition != null) && (paramMapSingleLayerReportDefinition.getCategoryName() != null))
    {
      this.areaNamePane.populateBean(paramMapSingleLayerReportDefinition.getCategoryName().toString());
      ArrayList localArrayList = new ArrayList();
      int i = paramMapSingleLayerReportDefinition.getTitleValueSize();
      for (int j = 0; j < i; j++)
      {
        SeriesDefinition localSeriesDefinition = paramMapSingleLayerReportDefinition.getTitleValueWithIndex(j);
        if ((localSeriesDefinition != null) && (localSeriesDefinition.getSeriesName() != null) && (localSeriesDefinition.getValue() != null))
          localArrayList.add(new Object[] { localSeriesDefinition.getSeriesName(), localSeriesDefinition.getValue() });
      }
      if (localArrayList.size() > 0)
        this.tabPane.populateBean(localArrayList);
    }
  }
  public MapSingleLayerReportDefinition updateBean()
  {
    MapSingleLayerReportDefinition localMapSingleLayerReportDefinition = new MapSingleLayerReportDefinition();
    String str = this.areaNamePane.updateBean();
    if (Formula.canBeFormula(str))
      localMapSingleLayerReportDefinition.setCategoryName(new Formula(str));
    else
      localMapSingleLayerReportDefinition.setCategoryName(str);
    List localList = this.tabPane.updateBean();
    int i = 0;
    int j = localList.size();
    while (i < j)
    {
      Object[] arrayOfObject = (Object[])localList.get(i);
      if (arrayOfObject.length == 2)
      {
        SeriesDefinition localSeriesDefinition = new SeriesDefinition();
        localSeriesDefinition.setSeriesName(arrayOfObject[0]);
        localSeriesDefinition.setValue(arrayOfObject[1]);
localMapSingleLayerReportDefinition.addTitleValue(localSeriesDefinition);
      }
      i++;
    }
    return localMapSingleLayerReportDefinition;
  }
  protected String title4PopupWindow()
  {
    return this.title;
  }
  private class InnerTableEditor extends UITableEditor
  {
    private JComponent editorComponent;
    private InnerTableEditor()
    {
    }
    public Object getCellEditorValue()
    {
      if ((this.editorComponent instanceof TinyFormulaPane))
        return ((TinyFormulaPane)this.editorComponent).getUITextField().getText();
      if ((this.editorComponent instanceof UITextField))
        return ((UITextField)this.editorComponent).getText();
      return super.getCellEditorValue();
    }
    public Component getTableCellEditorComponent(JTable paramJTable, Object paramObject, boolean paramBoolean, int paramInt1, int paramInt2)
    {
      if (paramInt2 == paramJTable.getModel().getColumnCount())
        return null;
      JComponent localJComponent = getEditorComponent(paramInt2, paramObject);
      return localJComponent;
    }
    private JComponent getEditorComponent(int paramInt, Object paramObject)
    {
      Object localObject;
      if (paramInt == 0)
      {
        localObject = new UITextField();
        this.editorComponent = ((JComponent)localObject);
        if (paramObject != null)
          ((UITextField)localObject).setText(paramObject.toString());
      }
      else
      {
        localObject = new TinyFormulaPane()
        {
          public void okEvent()
          {
            MapMoreReportIndexPane.this.tabPane.stopCellEditing();
            MapMoreReportIndexPane.this.tabPane.fireTargetChanged();
          }
        };
((TinyFormulaPane)localObject).setBackground(FRSwingConstants.FLESH_BLUE);
        ((TinyFormulaPane)localObject).getUITextField().addFocusListener(new FocusAdapter()
        {
          public void focusLost(FocusEvent paramAnonymousFocusEvent)
          {
            MapMoreReportIndexPane.this.tabPane.fireTargetChanged();
          }
        });
        if (paramObject != null)
((TinyFormulaPane)localObject).getUITextField().setText(paramObject.toString());
        this.editorComponent = ((JComponent)localObject);
      }
      return this.editorComponent;
    }
  }
}package com.fr.chart.chartData.reportData;
import com.fr.chart.chartdata.MapSingleLayerTableDefinition;
import com.fr.chart.chartdata.SeriesDefinition;
import com.fr.design.beans.BasicBeanPane;
import com.fr.design.gui.frpane.UICorrelationPane;
import com.fr.design.gui.icombobox.UIComboBox;
import com.fr.design.gui.ilable.UILabel;
import com.fr.design.gui.itable.UITableEditor;
import com.fr.design.gui.itextfield.UITextField;
import com.fr.general.Inter;
import com.fr.stable.StringUtils;
import java.awt.BorderLayout;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.util.ArrayList;
import java.util.List;
import javax.swing.ComboBoxModel;
import javax.swing.JComponent;
import javax.swing.JPanel;
import javax.swing.JTable;
import javax.swing.table.TableModel;
public class MapMoreTableIndexPane extends BasicBeanPane<MapSingleLayerTableDefinition>
{
  private static final long serialVersionUID = 8135457041761804584L;
  private String title = "";
  private UIComboBox areaNameBox;
  private UICorrelationPane tabPane;
  private Object[] boxItems = { "" };
  public MapMoreTableIndexPane()
  {
    initPane();
  }
  public MapMoreTableIndexPane(String paramString)
  {
    this.title = paramString;
    initPane();
  }
  protected String title4PopupWindow()
  {
    return this.title;
  }
  private void initPane()
  {
    setLayout(new BorderLayout());
    JPanel localJPanel = new JPanel();
    add(localJPanel, "North");
    localJPanel.setLayout(new FlowLayout(0));
    localJPanel.add(new UILabel(Inter.getLocText("Area_Name") + ":"));
    this.areaNameBox = new UIComboBox();
    this.areaNameBox.setPreferredSize(new Dimension(120, 20));
    localJPanel.add(this.areaNameBox);
    this.tabPane = new UICorrelationPane(new String[] { Inter.getLocLongText("Filed", "Title"), Inter.getLocText("Area_Value") })
    {
      public UITableEditor createUITableEditor()
      {
        return new MapMoreTableIndexPane.InnerTableEditor(MapMoreTableIndexPane.this, null);
      }
    };
    add(this.tabPane, "Center");
  }
  public void initAreaComBox(Object[] paramArrayOfObject)
  {
    Object localObject = this.areaNameBox.getSelectedItem();
    this.areaNameBox.removeAllItems();
    this.boxItems = paramArrayOfObject;
    if (paramArrayOfObject != null)
    {
      int i = 0;
      int j = paramArrayOfObject.length;
      while (i < j)
      {
        this.areaNameBox.addItem(paramArrayOfObject[i]);
        i++;
      }
    }
    this.areaNameBox.getModel().setSelectedItem(localObject);
  }
  public void populateBean(MapSingleLayerTableDefinition paramMapSingleLayerTableDefinition)
  {
    if (paramMapSingleLayerTableDefinition != null)
    {
      this.areaNameBox.setSelectedItem(paramMapSingleLayerTableDefinition.getAreaName());
      ArrayList localArrayList = new ArrayList();
      int i = paramMapSingleLayerTableDefinition.getTitleValueSize();
      for (int j = 0; j < i; j++)
      {
        SeriesDefinition localSeriesDefinition = paramMapSingleLayerTableDefinition.getTitleValueWithIndex(j);
        if ((localSeriesDefinition != null) &&(localSeriesDefinition.getSeriesName() != null) && (localSeriesDefinition.getValue() != null))
          localArrayList.add(new Object[] { localSeriesDefinition.getSeriesName(), localSeriesDefinition.getValue() });
      }
      if (localArrayList.size() > 0)
        this.tabPane.populateBean(localArrayList);
    }
  }
  public MapSingleLayerTableDefinition updateBean()
  {
    MapSingleLayerTableDefinition localMapSingleLayerTableDefinition = new MapSingleLayerTableDefinition();
    if (this.areaNameBox.getSelectedItem() != null)
      localMapSingleLayerTableDefinition.setAreaName(this.areaNameBox.getSelectedItem().toString());
    List localList = this.tabPane.updateBean();
    int i = 0;
    int j = localList.size();
    while (i < j)
    {
      Object[] arrayOfObject = (Object[])localList.get(i);
      if (arrayOfObject.length == 2)
      {
        SeriesDefinition localSeriesDefinition = new SeriesDefinition();
        localSeriesDefinition.setSeriesName(arrayOfObject[0]);
        localSeriesDefinition.setValue(arrayOfObject[1]);
localMapSingleLayerTableDefinition.addTitleValue(localSeriesDefinition);
      }
      i++;
    }
    return localMapSingleLayerTableDefinition;
  }
  private class InnerTableEditor extends UITableEditor
  {
    private JComponent editorComponent;
    private InnerTableEditor()
    {
    }
    public Object getCellEditorValue()
    {
      if ((this.editorComponent instanceof UIComboBox))
        return ((UIComboBox)this.editorComponent).getSelectedItem();
      if ((this.editorComponent instanceof UITextField))
        return ((UITextField)this.editorComponent).getText();
      return super.getCellEditorValue();
    }
    public Component getTableCellEditorComponent(JTable paramJTable, Object paramObject, boolean paramBoolean, int paramInt1, int paramInt2)
    {
      if (paramInt2 == paramJTable.getModel().getColumnCount())
        return null;
      return getEditorComponent(paramInt2, paramObject);
    }
    private JComponent getEditorComponent(int paramInt, Object paramObject)
    {
      Object localObject;
      if (paramInt == 0)
      {
        localObject = new UITextField();
        this.editorComponent = ((JComponent)localObject);
        if (paramObject != null)
          ((UITextField)localObject).setText(paramObject.toString());
      }
      else
      {
        localObject = new UIComboBox(MapMoreTableIndexPane.this.boxItems);
        ((UIComboBox)localObject).addItemListener(new ItemListener()
        {
          public void itemStateChanged(ItemEvent paramAnonymousItemEvent)
          {
            MapMoreTableIndexPane.this.tabPane.fireTargetChanged();
            MapMoreTableIndexPane.this.tabPane.stopCellEditing();
          }
        });
        if ((paramObject != null) &&(StringUtils.isNotEmpty(paramObject.toString())))
          ((UIComboBox)localObject).setSelectedItem(paramObject);
        else
          ((UIComboBox)localObject).setSelectedItem(paramObject);
        this.editorComponent = ((JComponent)localObject);
      }
      return this.editorComponent;
    }
  }
}
package com.fr.chart.chartData.reportData;
import com.fr.chart.chartdata.MapMoreLayerReportDefinition;
import com.fr.design.beans.FurtherBasicBeanPane;
import com.fr.design.event.UIObserver;
import com.fr.design.event.UIObserverListener;
import com.fr.dialog.BasicPane;
import com.fr.dialog.MultiTabPane;
import com.fr.general.Inter;
import java.awt.BorderLayout;
import java.util.ArrayList;
import java.util.List;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
  static final int LABEL_INSN = 8;
  static final int LABELW_INSN = 9;
  static final int LDC_INSN = 10;
  static final int LDCW_INSN = 11;
  static final int IINC_INSN = 12;
  static final int TABL_INSN = 13;
  static final int LOOK_INSN = 14;
  static final int MANA_INSN = 15;
  static final int WIDE_INSN = 16;
  static byte[] TYPE = arrayOfByte;
public class MapReportCubeDataPane extends FurtherBasicBeanPane<MapMoreLayerReportDefinition>
  implements UIObserver
{
  private int editingLayerCout = 0;
  private ArrayList<ChangeListener> changeListeners = new ArrayList();
  private TabPane tabPane;
  public MapReportCubeDataPane()
  {
    setLayout(new BorderLayout(0, 0));
    this.tabPane = new TabPane(null);
    add(this.tabPane, "Center");
  }
  public void setEditingLayer(int paramInt)
  {
    this.editingLayerCout = paramInt;
    initPaneRow();
  }
  private void initPaneRow()
  {
    this.tabPane.refreshWithLayerCount();
  }
  public boolean accept(Object paramObject)
  {
    return paramObject instanceof MapMoreLayerReportDefinition;
  }
  public void reset()
  {
  }
  public String title4PopupWindow()
  {
    return Inter.getLocText("Cell");
  }
  public void populateBean(MapMoreLayerReportDefinition paramMapMoreLayerReportDefinition)
  {
    initPaneRow();
    if (paramMapMoreLayerReportDefinition != null)
      this.tabPane.populateBean(paramMapMoreLayerReportDefinition);
  }
  public MapMoreLayerReportDefinition updateBean()
  {
    MapMoreLayerReportDefinition localMapMoreLayerReportDefinition = new MapMoreLayerReportDefinition();
    this.tabPane.updateBean(localMapMoreLayerReportDefinition);
    return localMapMoreLayerReportDefinition;
  }
  public void registerChangeListener(final UIObserverListener paramUIObserverListener)
  {
    this.changeListeners.add(new ChangeListener()
    {
      public void stateChanged(ChangeEvent paramAnonymousChangeEvent)
      {
        paramUIObserverListener.doChange();
      }
    });
  }
  public boolean shouldResponseChangeListener()
  {
    return true;
  }
  private class TabPane extends MultiTabPane<MapMoreLayerReportDefinition>
  {
    private TabPane()
    {
    }
    protected List<BasicPane> initPaneList()
    {
      ArrayList localArrayList = new ArrayList();
      localArrayList.add(new MapMoreReportIndexPane("1"));
      return localArrayList;
    }
    public void populateBean(MapMoreLayerReportDefinition paramMapMoreLayerReportDefinition)
    {
      int i = this.paneList.size();
      for (int j = 0; j < i; j++)
      {
        MapMoreReportIndexPane localMapMoreReportIndexPane = (MapMoreReportIndexPane)this.paneList.get(j);
        localMapMoreReportIndexPane.populateBean(paramMapMoreLayerReportDefinition.getValueWithLayerIndex(j));
      }
    }
    public void updateBean(MapMoreLayerReportDefinition paramMapMoreLayerReportDefinition)
    {
      paramMapMoreLayerReportDefinition.clearNameValues();
      int i = 0;
      int j = this.paneList.size();
      while (i < j)
      {
        MapMoreReportIndexPane localMapMoreReportIndexPane = (MapMoreReportIndexPane)this.paneList.get(i);
        paramMapMoreLayerReportDefinition.addNameValue(localMapMoreReportIndexPane.updateBean());
        i++;
      }
    }
    public boolean accept(Object paramObject)
    {
      return paramObject instanceof MapMoreLayerReportDefinition;
    }
    public void reset()
    {
    }
    public String title4PopupWindow()
    {
      return "";
    }
    public MapMoreLayerReportDefinition updateBean()
    {
      return null;
    }
    public void refreshWithLayerCount()
    {
      this.paneList.clear();
      for (int i = 0; i < MapReportCubeDataPane.this.editingLayerCout; i++)
      {
        int j = i + 1;
        this.paneList.add(new MapMoreReportIndexPane("" + j));
      }
      removeAll();
      relayoutWhenListChange();
    }
  }
}
package com.fr.chart.chartData.reportData;
import com.fr.base.Formula;
import com.fr.chart.chartdata.MapSingleLayerReportDefinition;
import com.fr.chart.chartdata.SeriesDefinition;
import com.fr.constants.FRSwingConstants;
import com.fr.design.beans.FurtherBasicBeanPane;
import com.fr.design.event.UIObserver;
import com.fr.design.event.UIObserverListener;
import com.fr.design.formula.TinyFormulaPane;
import com.fr.design.gui.frpane.UICorrelationPane;
import com.fr.design.gui.ilable.UILabel;
import com.fr.design.gui.itable.UITableEditor;
import com.fr.design.gui.itextfield.UITextField;
import com.fr.general.Inter;
import java.awt.BorderLayout;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;
import java.util.ArrayList;
import java.util.List;
import javax.swing.JComponent;
import javax.swing.JPanel;
import javax.swing.JTable;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.table.TableModel;
public class MapReportDataSinglePane extends FurtherBasicBeanPane<MapSingleLayerReportDefinition>
  implements UIObserver
{
  private TinyFormulaPane areaNamePane;
  private UICorrelationPane seriesPane;
  private ArrayList<ChangeListener> changeListeners = new ArrayList();
  public MapReportDataSinglePane()
  {
    initCom();
  }
  private void initCom()
  {
    setLayout(new BorderLayout(0, 0));
    JPanel localJPanel = new JPanel();
    add(localJPanel, "North");
    localJPanel.setLayout(new FlowLayout(1));
    localJPanel.add(new UILabel(Inter.getLocText("Area_Name") + ":", 4));
    this.areaNamePane = new TinyFormulaPane();
    this.areaNamePane.setPreferredSize(new Dimension(120, 20));
    localJPanel.add(this.areaNamePane);
    String[] arrayOfString = { Inter.getLocLongText("Filed", "Title"), Inter.getLocText("Area_Value") };
    this.seriesPane = new UICorrelationPane(arrayOfString)
    {
      public UITableEditor createUITableEditor()
      {
        return new MapReportDataSinglePane.InnerTableEditor(MapReportDataSinglePane.this, null);
      }
    };
    add(this.seriesPane, "Center");
  }
  public boolean accept(Object paramObject)
  {
    return true;
  }
  public void reset()
  {
  }
  public String title4PopupWindow()
  {
    return Inter.getLocText("Cell");
  }
  public void populateBean(MapSingleLayerReportDefinition paramMapSingleLayerReportDefinition)
  {
    if (paramMapSingleLayerReportDefinition.getCategoryName() != null)
    {
      this.areaNamePane.populateBean(paramMapSingleLayerReportDefinition.getCategoryName().toString());
      int i = paramMapSingleLayerReportDefinition.getTitleValueSize();
      ArrayList localArrayList = new ArrayList();
      for (int j = 0; j < i; j++)
      {
        SeriesDefinition localSeriesDefinition = paramMapSingleLayerReportDefinition.getTitleValueWithIndex(j);
        if ((localSeriesDefinition != null) &&(localSeriesDefinition.getSeriesName() != null) && (localSeriesDefinition.getValue() != null))
          localArrayList.add(new Object[] { localSeriesDefinition.getSeriesName(), localSeriesDefinition.getValue() });
      }
      if (localArrayList.size() > 0)
        this.seriesPane.populateBean(localArrayList);
    }
  }
  public MapSingleLayerReportDefinition updateBean()
  {
    MapSingleLayerReportDefinition localMapSingleLayerReportDefinition = new MapSingleLayerReportDefinition();
    String str = this.areaNamePane.updateBean();
    if (Formula.canBeFormula(str))
      localMapSingleLayerReportDefinition.setCategoryName(new Formula(str));
    else
      localMapSingleLayerReportDefinition.setCategoryName(str);
    List localList = this.seriesPane.updateBean();
    if ((localList != null) && (localList.size() > 0))
    {
      int i = 0;
      int j = localList.size();
      while (i < j)
      {
        Object[] arrayOfObject = (Object[])localList.get(i);
        Object localObject1 = arrayOfObject[0];
        Object localObject2 = arrayOfObject[1];
        if (Formula.canBeFormula(localObject2))
          localObject2 = new Formula(((Object)localObject2).toString());
        SeriesDefinition localSeriesDefinition = new SeriesDefinition(localObject1, localObject2);
        localMapSingleLayerReportDefinition.addTitleValue(localSeriesDefinition);
        i++;
      }
    }
    return localMapSingleLayerReportDefinition;
  }
  public void registerChangeListener(final UIObserverListener paramUIObserverListener)
  {
    this.changeListeners.add(new ChangeListener()
    {
      public void stateChanged(ChangeEvent paramAnonymousChangeEvent)
      {
        paramUIObserverListener.doChange();
      }
    });
  }
  public boolean shouldResponseChangeListener()
  {
    return true;
  }
  private class InnerTableEditor extends UITableEditor
  {
    private JComponent editorComponent;
    private InnerTableEditor()
    {
    }
    public Object getCellEditorValue()
    {
      if ((this.editorComponent instanceof TinyFormulaPane))
        return ((TinyFormulaPane)this.editorComponent).getUITextField().getText();
      if ((this.editorComponent instanceof UITextField))
        return ((UITextField)this.editorComponent).getText();
      return super.getCellEditorValue();
    }
    public Component getTableCellEditorComponent(JTable paramJTable, Object paramObject, boolean paramBoolean, int paramInt1, int paramInt2)
    {
      if (paramInt2 == paramJTable.getModel().getColumnCount())
        return null;
      return getEditorComponent(paramInt2, paramObject);
    }
    private JComponent getEditorComponent(int paramInt, Object paramObject)
    {
      Object localObject;
      if (paramInt == 0)
      {
        localObject = new UITextField();
        addListener4UITextFiled((UITextField)localObject);
        if (paramObject != null)
          ((UITextField)localObject).setText(paramObject.toString());
        this.editorComponent = ((JComponent)localObject);
      }
      else
      {
        localObject = new TinyFormulaPane()
        {
          public void okEvent()
          {
            MapReportDataSinglePane.this.seriesPane.stopCellEditing();
            MapReportDataSinglePane.this.seriesPane.fireTargetChanged();
          }
        };
((TinyFormulaPane)localObject).setBackground(FRSwingConstants.FLESH_BLUE);
addListener4UITextFiled(((TinyFormulaPane)localObject).getUITextField());
        if (paramObject != null)
((TinyFormulaPane)localObject).getUITextField().setText(paramObject.toString());
        this.editorComponent = ((JComponent)localObject);
      }
      return this.editorComponent;
    }
    private void addListener4UITextFiled(UITextField paramUITextField)
    {
      paramUITextField.addFocusListener(new FocusAdapter()
      {
        public void focusLost(FocusEvent paramAnonymousFocusEvent)
        {
          MapReportDataSinglePane.this.seriesPane.fireTargetChanged();
        }
      });
    }
  }
}
package com.fr.chart.chartData.reportData;
import com.fr.chart.chartData.ChartDemoPane;
import com.fr.chart.chartData.tableData.MapTableDefinitionPane;
import com.fr.chart.chartattr.Chart;
import com.fr.chart.chartdata.NormalReportDataDefinition;
import com.fr.chart.chartdata.SeriesDefinition;
import com.fr.chart.series.PlotSeries.MapDataPane;
import com.fr.design.gui.ilable.UILabel;
import com.fr.design.gui.itableeditorpane.UIArrayTableModel;
import com.fr.design.gui.itableeditorpane.UITableEditorPane;
import com.fr.design.layout.FRGUIPaneFactory;
import com.fr.general.Inter;
import java.awt.Dimension;
import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;
import java.util.List;
import javax.swing.JPanel;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
public class MapReportDefinitionPane extends AbstractReportDefinitionPane<NormalReportDataDefinition>
{
  private static final long serialVersionUID = -7004237114101358579L;
  private MapDataPane mapDataPane;
  DocumentListener documentListener = new DocumentListener()
  {
    public void removeUpdate(DocumentEvent paramAnonymousDocumentEvent)
    {
      MapReportDefinitionPane.this.chartDataChanged();
    }
    public void insertUpdate(DocumentEvent paramAnonymousDocumentEvent)
    {
      MapReportDefinitionPane.this.chartDataChanged();
    }
    public void changedUpdate(DocumentEvent paramAnonymousDocumentEvent)
    {
      MapReportDefinitionPane.this.chartDataChanged();
    }
  };
  FocusAdapter focusListener = new FocusAdapter()
  {
    public void focusLost(FocusEvent paramAnonymousFocusEvent)
    {
MapReportDefinitionPane.this.demoShowPane.setHighlight(ChartDemoPane.NONE);
      MapReportDefinitionPane.this.chartDataChanged();
    }
    public void focusGained(FocusEvent paramAnonymousFocusEvent)
    {
      int i = ChartDemoPane.NONE;
      if (MapReportDefinitionPane.this.editorPane.getSelectedColumn() == 0)
        i = ChartDemoPane.SERIES;
      else if (MapReportDefinitionPane.this.editorPane.getSelectedColumn() == 1)
        i = ChartDemoPane.VALUE;
      MapReportDefinitionPane.this.demoShowPane.setHighlight(i);
    }
  };
  public MapReportDefinitionPane()
  {
    initComponents();
  }
  private void initComponents()
  {
    JPanel localJPanel1 = initPane();
    this.demoShowPane = new ChartDemoPane();
    this.mapDataPane = new MapDataPane();
    this.mapDataPane.setChartDemoPane(this.demoShowPane);
    localJPanel1.add(this.mapDataPane);
    localJPanel1.add(this.demoShowPane);
    JPanel localJPanel2 = new JPanel(FRGUIPaneFactory.createLabelFlowLayout());
    localJPanel1.add(localJPanel2);
    localJPanel2.add(new UILabel(Inter.getLocText(new String[] { "Chart_Legend(Series)", "Define" }) + ":"));
    this.model = new UIArrayTableModel(new String[] { Inter.getLocText(new String[] { "Chart_Legend(Series)", "WF-Name" }), Inter.getLocText(new String[] { "Chart_Legend(Series)", "Values" }) }, new int[] { 1, 2 });
    this.editorPane = new UITableEditorPane(this.model);
    this.editorPane.setPreferredSize(new Dimension(500, 170));
    localJPanel1.add(this.editorPane);
    renderEditorPane(new Class[] { Object.class, Object.class });
  }
  public void repaintDemoShow(Chart paramChart)
  {
    super.repaintDemoShow(paramChart);
    if (this.mapDataPane != null)
    {
      this.mapDataPane.inits();
      this.mapDataPane.populate(paramChart.getPlot());
    }
  }
  public Chart getChart()
  {
    return this.demoShowPane.getChart();
  }
  public void populate(NormalReportDataDefinition paramNormalReportDataDefinition)
  {
    if (paramNormalReportDataDefinition == null)
      return;
    this.editorPane.populate(populateSeriesEntryList(paramNormalReportDataDefinition));
    chartDataChanged();
  }
  public NormalReportDataDefinition update()
  {
    NormalReportDataDefinition localNormalReportDataDefinition = new NormalReportDataDefinition();
    localNormalReportDataDefinition.setCategoryName(Inter.getLocText("Chart-Map"));
    updateSeriesEntryList(localNormalReportDataDefinition, this.editorPane.update());
    return localNormalReportDataDefinition;
  }
  private Object[][] populateSeriesEntryList(NormalReportDataDefinition paramNormalReportDataDefinition)
  {
    Object[][] arrayOfObject; = new Object[paramNormalReportDataDefinition.size()][];
    for (int i = 0; i < paramNormalReportDataDefinition.size(); i++)
    {
      SeriesDefinition localSeriesDefinition = (SeriesDefinition)paramNormalReportDataDefinition.get(i);
      Object[] arrayOfObject = new Object[2];
      arrayOfObject[0] = localSeriesDefinition.getSeriesName();
      arrayOfObject[1] = localSeriesDefinition.getValue();
      arrayOfObject;[i] = arrayOfObject;
    }
    return arrayOfObject;;
  }
  private void updateSeriesEntryList(NormalReportDataDefinition paramNormalReportDataDefinition, List<Object[]> paramList)
  {
    for (int i = 0; i < paramList.size(); i++)
    {
      Object[] arrayOfObject = (Object[])paramList.get(i);
      if ((arrayOfObject[0] != null) && (arrayOfObject[1] != null))
      {
        SeriesDefinition localSeriesDefinition = new SeriesDefinition();
        localSeriesDefinition.setSeriesName(arrayOfObject[0]);
        localSeriesDefinition.setValue(arrayOfObject[1]);
        paramNormalReportDataDefinition.add(localSeriesDefinition);
      }
    }
  }
  protected void chartDataChanged()
  {
    this.demoShowPane.repaintChartData(MapTableDefinitionPane.createChartData4EveryType());
  }
  protected FocusAdapter getFocust4SelectCom()
  {
    return this.focusListener;
  }
}
package org.slf4j.impl;
import org.apache.log4j.Level;
import org.apache.log4j.Logger;
import org.slf4j.Marker;
import org.slf4j.helpers.MarkerIgnoringBase;
import org.slf4j.helpers.MessageFormatter;
import org.slf4j.spi.LocationAwareLogger;
public final class Log4jLoggerAdapter extends MarkerIgnoringBase
  implements LocationAwareLogger
{
  final Logger logger;
  static final String FQCN = Log4jLoggerAdapter.class.getName();
  Log4jLoggerAdapter(Logger logger)
  {
    this.logger = logger;
  }
  public String getName() {
    return this.logger.getName();
  }
  public boolean isTraceEnabled()
  {
    return this.logger.isTraceEnabled();
  }
  public void trace(String msg)
  {
    this.logger.log(FQCN, Level.TRACE, msg, null);
  }
  public void trace(String format, Object arg)
  {
    if (this.logger.isTraceEnabled()) {
      String msgStr = MessageFormatter.format(format, arg);
      this.logger.log(FQCN, Level.TRACE, msgStr, null);
    }
  }
  public void trace(String format, Object arg1, Object arg2)
  {
    if (this.logger.isTraceEnabled()) {
      String msgStr = MessageFormatter.format(format, arg1, arg2);
      this.logger.log(FQCN, Level.TRACE, msgStr, null);
    }
  }
  public void trace(String format, Object[] argArray)
  {
    if (this.logger.isTraceEnabled()) {
      String msgStr = MessageFormatter.arrayFormat(format, argArray);
      this.logger.log(FQCN, Level.TRACE, msgStr, null);
    }
  }
  public void trace(String msg, Throwable t)
  {
    this.logger.log(FQCN, Level.TRACE, msg, t);
  }
  public boolean isDebugEnabled()
  {
    return this.logger.isDebugEnabled();
  }
  public void debug(String msg)
  {
    this.logger.log(FQCN, Level.DEBUG, msg, null);
  }
  public void debug(String format, Object arg)
  {
    if (this.logger.isDebugEnabled()) {
      String msgStr = MessageFormatter.format(format, arg);
      this.logger.log(FQCN, Level.DEBUG, msgStr, null);
    }
  }
  public void debug(String format, Object arg1, Object arg2)
  {
    if (this.logger.isDebugEnabled()) {
      String msgStr = MessageFormatter.format(format, arg1, arg2);
      this.logger.log(FQCN, Level.DEBUG, msgStr, null);
    }
  }
  public void debug(String format, Object[] argArray)
  {
    if (this.logger.isDebugEnabled()) {
      String msgStr = MessageFormatter.arrayFormat(format, argArray);
      this.logger.log(FQCN, Level.DEBUG, msgStr, null);
    }
  }
  public void debug(String msg, Throwable t)
  {
    this.logger.log(FQCN, Level.DEBUG, msg, t);
  }
  public boolean isInfoEnabled()
  {
    return this.logger.isInfoEnabled();
  }
  public void info(String msg)
  {
    this.logger.log(FQCN, Level.INFO, msg, null);
  }
  public void info(String format, Object arg)
  {
    if (this.logger.isInfoEnabled()) {
      String msgStr = MessageFormatter.format(format, arg);
      this.logger.log(FQCN, Level.INFO, msgStr, null);
    }
  }
  public void info(String format, Object arg1, Object arg2)
  {
    if (this.logger.isInfoEnabled()) {
      String msgStr = MessageFormatter.format(format, arg1, arg2);
      this.logger.log(FQCN, Level.INFO, msgStr, null);
    }
  }
  public void info(String format, Object[] argArray)
  {
    if (this.logger.isInfoEnabled()) {
      String msgStr = MessageFormatter.arrayFormat(format, argArray);
      this.logger.log(FQCN, Level.INFO, msgStr, null);
    }
  }
  public void info(String msg, Throwable t)
  {
    this.logger.log(FQCN, Level.INFO, msg, t);
  }
  public boolean isWarnEnabled()
  {
    return this.logger.isEnabledFor(Level.WARN);
  }
  public void warn(String msg)
  {
    this.logger.log(FQCN, Level.WARN, msg, null);
  }
  public void warn(String format, Object arg)
  {
    if (this.logger.isEnabledFor(Level.WARN)) {
      String msgStr = MessageFormatter.format(format, arg);
      this.logger.log(FQCN, Level.WARN, msgStr, null);
    }
  }
  public void warn(String format, Object arg1, Object arg2)
  {
    if (this.logger.isEnabledFor(Level.WARN)) {
      String msgStr = MessageFormatter.format(format, arg1, arg2);
      this.logger.log(FQCN, Level.WARN, msgStr, null);
    }
  }
  public void warn(String format, Object[] argArray)
  {
    if (this.logger.isEnabledFor(Level.WARN)) {
      String msgStr = MessageFormatter.arrayFormat(format, argArray);
      this.logger.log(FQCN, Level.WARN, msgStr, null);
    }
  }
  public void warn(String msg, Throwable t)
  {
    this.logger.log(FQCN, Level.WARN, msg, t);
  }
  public boolean isErrorEnabled()
  {
    return this.logger.isEnabledFor(Level.ERROR);
  }
  public void error(String msg)
  {
    this.logger.log(FQCN, Level.ERROR, msg, null);
  }
  public void error(String format, Object arg)
  {
    if (this.logger.isEnabledFor(Level.ERROR)) {
      String msgStr = MessageFormatter.format(format, arg);
      this.logger.log(FQCN, Level.ERROR, msgStr, null);
    }
  }
  public void error(String format, Object arg1, Object arg2)
  {
    if (this.logger.isEnabledFor(Level.ERROR)) {
      String msgStr = MessageFormatter.format(format, arg1, arg2);
      this.logger.log(FQCN, Level.ERROR, msgStr, null);
    }
  }
  public void error(String format, Object[] argArray)
  {
    if (this.logger.isEnabledFor(Level.ERROR)) {
      String msgStr = MessageFormatter.arrayFormat(format, argArray);
      this.logger.log(FQCN, Level.ERROR, msgStr, null);
    }
  }
  public void error(String msg, Throwable t)
  {
    this.logger.log(FQCN, Level.ERROR, msg, t);
  }
  public void log(Marker marker, String callerFQCN, int level, String msg, Throwable t)
  {
    Level log4jLevel;
    switch (level) {
    case 0:
      log4jLevel = Level.TRACE;
      break;
    case 10:
      log4jLevel = Level.DEBUG;
      break;
    case 20:
      log4jLevel = Level.INFO;
      break;
    case 30:
      log4jLevel = Level.WARN;
      break;
    case 40:
      log4jLevel = Level.ERROR;
      break;
    default:
      throw new IllegalStateException("Level number " + level + " is not recognized.");
    }
    this.logger.log(callerFQCN, log4jLevel, msg, t);
  }
}
package org.slf4j.impl;
import java.util.HashMap;
import java.util.Map;
import org.apache.log4j.LogManager;
import org.slf4j.ILoggerFactory;
public class Log4jLoggerFactory
  implements ILoggerFactory
{
  Map loggerMap;
  public Log4jLoggerFactory()
  {
    this.loggerMap = new HashMap();
  }
  public org.slf4j.Logger getLogger(String name)
  {
    org.slf4j.Logger slf4jLogger = null;
    synchronized (this) {
      slf4jLogger = (org.slf4j.Logger)this.loggerMap.get(name);
      if (slf4jLogger == null)
      {
        org.apache.log4j.Logger log4jLogger;
        org.apache.log4j.Logger log4jLogger;
        if (name.equalsIgnoreCase("ROOT"))
          log4jLogger = LogManager.getRootLogger();
        else {
          log4jLogger = LogManager.getLogger(name);
        }
        slf4jLogger = new Log4jLoggerAdapter(log4jLogger);
        this.loggerMap.put(name, slf4jLogger);
      }
    }
    return slf4jLogger;
  }
}package org.slf4j.impl;
import java.util.Map;
import org.apache.log4j.MDC;
import org.slf4j.spi.MDCAdapter;
public class Log4jMDCAdapter
  implements MDCAdapter
{
  public void clear()
  {
    Map map = MDC.getContext();
    if (map != null)
      map.clear();
  }
  public String get(String key)
  {
    return (String)MDC.get(key);
  }
  public void put(String key, String val)
  {
    MDC.put(key, val);
  }
  public void remove(String key) {
    MDC.remove(key);
  }
}package org.slf4j.impl;
import org.apache.log4j.Level;
import org.slf4j.ILoggerFactory;
import org.slf4j.spi.LoggerFactoryBinder;
public class StaticLoggerBinder
  implements LoggerFactoryBinder
{
  public static final StaticLoggerBinder SINGLETON = new StaticLoggerBinder();
  private static final String loggerFactoryClassStr = Log4jLoggerFactory.class.getName();
  private final ILoggerFactory loggerFactory;
  private StaticLoggerBinder()
  {
    this.loggerFactory = new Log4jLoggerFactory();
    try {
      level = Level.TRACE;
    }
    catch (NoSuchFieldError nsfe)
    {
      Level level;
      throw new Error("This version of SLF4J requires log4j version 1.2.12 or later. See also http:    }
  }
  public ILoggerFactory getLoggerFactory() {
    return this.loggerFactory;
  }
  public String getLoggerFactoryClassStr() {
    return loggerFactoryClassStr;
  }
}package org.objectweb.asm;
public class Attribute
{
  public final String type;
  public Attribute next;
  protected Attribute(String paramString)
  {
    this.type = paramString;
  }
  public boolean isUnknown()
  {
    return getClass().getName().equals("org.objectweb.asm.Attribute");
  }
  protected Label[] getLabels()
  {
    return null;
  }
  protected Attribute read(ClassReader paramClassReader, int paramInt1, int paramInt2, char[] paramArrayOfChar, int paramInt3, Label[] paramArrayOfLabel)
  {
    return new Attribute(this.type);
  }
  protected ByteVector write(ClassWriter paramClassWriter, byte[] paramArrayOfByte, int paramInt1, int paramInt2, int paramInt3)
  {
    return new ByteVector();
  }
  final int getCount()
  {
    int i = 0;
    for (Attribute localAttribute = this; localAttribute != null; localAttribute = localAttribute.next)
      if (!localAttribute.isUnknown())
        i++;
    return i;
  }
  final int getSize(ClassWriter paramClassWriter, byte[] paramArrayOfByte, int paramInt1, int paramInt2, int paramInt3)
  {
    int i = 0;
    for (Attribute localAttribute = this; localAttribute != null; localAttribute = localAttribute.next)
    {
      ByteVector localByteVector = localAttribute.write(paramClassWriter, paramArrayOfByte, paramInt1, paramInt2, paramInt3);
      if (localByteVector.length > 0)
      {
        paramClassWriter.newUTF8(localAttribute.type);
        i += localByteVector.length + 6;
      }
    }
    return i;
  }
  final void put(ClassWriter paramClassWriter, byte[] paramArrayOfByte, int paramInt1, int paramInt2, int paramInt3, ByteVector paramByteVector)
  {
    if (this.next != null)
      this.next.put(paramClassWriter, paramArrayOfByte, paramInt1, paramInt2, paramInt3, paramByteVector);
    ByteVector localByteVector = write(paramClassWriter, paramArrayOfByte, paramInt1, paramInt2, paramInt3);
    if (localByteVector.length == 0)
    {
      if (paramClassWriter.checkAttributes)
        throw new IllegalArgumentException("Unknown attribute type " + this.type);
    }
    else
    {
      paramByteVector.putShort(paramClassWriter.newUTF8(this.type)).putInt(localByteVector.length);
      paramByteVector.putByteArray(localByteVector.data, 0, localByteVector.length);
    }
  }
}
package org.objectweb.asm;
public class ByteVector
{
  byte[] data;
  int length;
  public ByteVector()
  {
    this.data = new byte[64];
  }
  public ByteVector(int paramInt)
  {
    this.data = new byte[paramInt];
  }
  public ByteVector putByte(int paramInt)
  {
    int i = this.length;
    if (i + 1 > this.data.length)
      enlarge(1);
    this.data[(i++)] = ((byte)paramInt);
    this.length = i;
    return this;
  }
  ByteVector put11(int paramInt1, int paramInt2)
  {
    int i = this.length;
    if (i + 2 > this.data.length)
      enlarge(2);
    byte[] arrayOfByte = this.data;
    arrayOfByte[(i++)] = ((byte)paramInt1);
    arrayOfByte[(i++)] = ((byte)paramInt2);
    this.length = i;
    return this;
  }
  public ByteVector putShort(int paramInt)
  {
    int i = this.length;
    if (i + 2 > this.data.length)
      enlarge(2);
    byte[] arrayOfByte = this.data;
    arrayOfByte[(i++)] = ((byte)(paramInt >>> 8));
    arrayOfByte[(i++)] = ((byte)paramInt);
    this.length = i;
    return this;
  }
  ByteVector put12(int paramInt1, int paramInt2)
  {
    int i = this.length;
    if (i + 3 > this.data.length)
      enlarge(3);
    byte[] arrayOfByte = this.data;
    arrayOfByte[(i++)] = ((byte)paramInt1);
    arrayOfByte[(i++)] = ((byte)(paramInt2 >>> 8));
    arrayOfByte[(i++)] = ((byte)paramInt2);
    this.length = i;
    return this;
  }
  public ByteVector putInt(int paramInt)
  {
    int i = this.length;
    if (i + 4 > this.data.length)
      enlarge(4);
    byte[] arrayOfByte = this.data;
    arrayOfByte[(i++)] = ((byte)(paramInt >>> 24));
    arrayOfByte[(i++)] = ((byte)(paramInt >>> 16));
    arrayOfByte[(i++)] = ((byte)(paramInt >>> 8));
    arrayOfByte[(i++)] = ((byte)paramInt);
    this.length = i;
    return this;
  }
  public ByteVector putLong(long paramLong)
  {
    int i = this.length;
    if (i + 8 > this.data.length)
      enlarge(8);
    byte[] arrayOfByte = this.data;
    int j = (int)(paramLong >>> 32);
    arrayOfByte[(i++)] = ((byte)(j >>> 24));
    arrayOfByte[(i++)] = ((byte)(j >>> 16));
    arrayOfByte[(i++)] = ((byte)(j >>> 8));
    arrayOfByte[(i++)] = ((byte)j);
    j = (int)paramLong;
    arrayOfByte[(i++)] = ((byte)(j >>> 24));
    arrayOfByte[(i++)] = ((byte)(j >>> 16));
    arrayOfByte[(i++)] = ((byte)(j >>> 8));
    arrayOfByte[(i++)] = ((byte)j);
    this.length = i;
    return this;
  }
  public ByteVector putUTF8(String paramString)
  {
    int i = paramString.length();
    int j = 0;
    for (int k = 0; k < i; k++)
    {
      int m = paramString.charAt(k);
      if ((m >= 1) && (m <= 127))
        j++;
      else if (m > 2047)
        j += 3;
      else
        j += 2;
    }
    if (j > 65535)
      throw new IllegalArgumentException();
    k = this.length;
    if (k + 2 + j > this.data.length)
      enlarge(2 + j);
    byte[] arrayOfByte = this.data;
    arrayOfByte[(k++)] = ((byte)(j >>> 8));
    arrayOfByte[(k++)] = ((byte)j);
    for (int n = 0; n < i; n++)
    {
      int i1 = paramString.charAt(n);
      if ((i1 >= 1) && (i1 <= 127))
      {
        arrayOfByte[(k++)] = ((byte)i1);
      }
      else if (i1 > 2047)
      {
        arrayOfByte[(k++)] = ((byte)(0xE0 | i1 >> 12 & 0xF));
        arrayOfByte[(k++)] = ((byte)(0x80 | i1 >> 6 & 0x3F));
        arrayOfByte[(k++)] = ((byte)(0x80 | i1 & 0x3F));
      }
      else
      {
        arrayOfByte[(k++)] = ((byte)(0xC0 | i1 >> 6 & 0x1F));
        arrayOfByte[(k++)] = ((byte)(0x80 | i1 & 0x3F));
      }
    }
    this.length = k;
    return this;
  }
  public ByteVector putByteArray(byte[] paramArrayOfByte, int paramInt1, int paramInt2)
  {
    if (this.length + paramInt2 > this.data.length)
      enlarge(paramInt2);
    if (paramArrayOfByte != null)
      System.arraycopy(paramArrayOfByte, paramInt1, this.data, this.length, paramInt2);
    this.length += paramInt2;
    return this;
  }
  private void enlarge(int paramInt)
  {
    int i = 2 * this.data.length;
    int j = this.length + paramInt;
    byte[] arrayOfByte = new byte[i > j ? i : j];
    System.arraycopy(this.data, 0, arrayOfByte, 0, this.length);
    this.data = arrayOfByte;
  }
}package org.objectweb.asm;
public class ClassAdapter
  implements ClassVisitor
{
  protected ClassVisitor cv;
  public ClassAdapter(ClassVisitor paramClassVisitor)
  {
    this.cv = paramClassVisitor;
  }
  public void visit(int paramInt1, int paramInt2, String paramString1, String paramString2, String[] paramArrayOfString, String paramString3)
  {
    this.cv.visit(paramInt1, paramInt2, paramString1, paramString2, paramArrayOfString, paramString3);
  }
  public void visitInnerClass(String paramString1, String paramString2, String paramString3, int paramInt)
  {
    this.cv.visitInnerClass(paramString1, paramString2, paramString3, paramInt);
  }
  public void visitField(int paramInt, String paramString1, String paramString2, Object paramObject, Attribute paramAttribute)
  {
    this.cv.visitField(paramInt, paramString1, paramString2, paramObject, paramAttribute);
  }
  public CodeVisitor visitMethod(int paramInt, String paramString1, String paramString2, String[] paramArrayOfString, Attribute paramAttribute)
  {
    return new CodeAdapter(this.cv.visitMethod(paramInt, paramString1, paramString2, paramArrayOfString, paramAttribute));
  }
  public void visitAttribute(Attribute paramAttribute)
  {
    this.cv.visitAttribute(paramAttribute);
  }
  public void visitEnd()
  {
    this.cv.visitEnd();
  }
}package org.objectweb.asm;
public class ClassWriter
  implements ClassVisitor
{
  static final int CLASS = 7;
  static final int FIELD = 9;
  static final int METH = 10;
  static final int IMETH = 11;
  static final int STR = 8;
  static final int INT = 3;
  static final int FLOAT = 4;
  static final int LONG = 5;
  static final int DOUBLE = 6;
  static final int NAME_TYPE = 12;
  static final int UTF8 = 1;
  private int version;
  private short index = 1;
  private ByteVector pool = new ByteVector();
  private Item[] items = new Item[64];
  private int threshold = (int)(0.75D * this.items.length);
  private int access;
  private int name;
  private int superName;
  private int interfaceCount;
  private int[] interfaces;
  private int sourceFile;
  private int fieldCount;
  private ByteVector fields;
  private boolean computeMaxs;
  boolean checkAttributes;
  CodeWriter firstMethod;
  CodeWriter lastMethod;
  private int innerClassesCount;
  private ByteVector innerClasses;
  private Attribute attrs;
  Item key = new Item();
  Item key2 = new Item();
  Item key3 = new Item();
  static final int NOARG_INSN = 0;
  static final int SBYTE_INSN = 1;
  static final int SHORT_INSN = 2;
  static final int VAR_INSN = 3;
  static final int IMPLVAR_INSN = 4;
  static final int TYPE_INSN = 5;
  static final int FIELDORMETH_INSN = 6;
  static final int ITFMETH_INSN = 7;
  static final int LABEL_INSN = 8;
  static final int LABELW_INSN = 9;
  static final int LDC_INSN = 10;
  static final int LDCW_INSN = 11;
  static final int IINC_INSN = 12;
  static final int TABL_INSN = 13;
  static final int LOOK_INSN = 14;
  static final int MANA_INSN = 15;
  static final int WIDE_INSN = 16;
  static byte[] TYPE = arrayOfByte;
  public ClassWriter(boolean paramBoolean)
  {
    this(paramBoolean, false);
  }
  public ClassWriter(boolean paramBoolean1, boolean paramBoolean2)
  {
    this.computeMaxs = paramBoolean1;
    this.checkAttributes = (!paramBoolean2);
  }
  public void visit(int paramInt1, int paramInt2, String paramString1, String paramString2, String[] paramArrayOfString, String paramString3)
  {
    this.version = paramInt1;
    this.access = paramInt2;
    this.name = newClass(paramString1);
    this.superName = (paramString2 == null ? 0 : newClass(paramString2));
    if ((paramArrayOfString != null) && (paramArrayOfString.length > 0))
    {
      this.interfaceCount = paramArrayOfString.length;
      this.interfaces = new int[this.interfaceCount];
      for (int i = 0; i < this.interfaceCount; i++)
        this.interfaces[i] = newClass(paramArrayOfString[i]);
    }
    if (paramString3 != null)
    {
      newUTF8("SourceFile");
      this.sourceFile = newUTF8(paramString3);
    }
    if ((paramInt2 & 0x20000) != 0)
      newUTF8("Deprecated");
    if ((paramInt2 & 0x1000) != 0)
      newUTF8("Synthetic");
  }
  public void visitInnerClass(String paramString1, String paramString2, String paramString3, int paramInt)
  {
    if (this.innerClasses == null)
    {
      newUTF8("InnerClasses");
         this.innerClasses = new ByteVector();
    }
    this.innerClassesCount += 1;
    this.innerClasses.putShort(paramString1 == null ? 0 : newClass(paramString1));
    this.innerClasses.putShort(paramString2 == null ? 0 : newClass(paramString2));
    this.innerClasses.putShort(paramString3 == null ? 0 : newUTF8(paramString3));
    this.innerClasses.putShort(paramInt);
  }
  public void visitField(int paramInt, String paramString1, String paramString2, Object paramObject, Attribute paramAttribute)
  {
    this.fieldCount += 1;
    if (this.fields == null)
      this.fields = new ByteVector();
    this.fields.putShort(paramInt).putShort(newUTF8(paramString1)).putShort(newUTF8(paramString2));
    int i = 0;
    if (paramObject != null)
      i++;
    if ((paramInt & 0x1000) != 0)
      i++;
    if ((paramInt & 0x20000) != 0)
      i++;
    if (paramAttribute != null)
      i += paramAttribute.getCount();
    this.fields.putShort(i);
    if (paramObject != null)
    {
      this.fields.putShort(newUTF8("ConstantValue"));
      this.fields.putInt(2).putShort(newConstItem(paramObject).index);
    }
    if ((paramInt & 0x1000) != 0)
      this.fields.putShort(newUTF8("Synthetic")).putInt(0);
    if ((paramInt & 0x20000) != 0)
      this.fields.putShort(newUTF8("Deprecated")).putInt(0);
    if (paramAttribute != null)
      paramAttribute.put(this, null, 0, -1, -1, this.fields);
  }
  public CodeVisitor visitMethod(int paramInt, String paramString1, String paramString2, String[] paramArrayOfString, Attribute paramAttribute)
  {
    CodeWriter localCodeWriter = new CodeWriter(this, this.computeMaxs);
    localCodeWriter.init(paramInt, paramString1, paramString2, paramArrayOfString, paramAttribute);
    return localCodeWriter;
  }
  public void visitAttribute(Attribute paramAttribute)
  {
    paramAttribute.next = this.attrs;
    this.attrs = paramAttribute;
  }
  public void visitEnd()
  {
  }
  public byte[] toByteArray()
  {
    int i = 24 + 2 * this.interfaceCount;
    if (this.fields != null)
      i += this.fields.length;
    int j = 0;
    for (CodeWriter localCodeWriter = this.firstMethod; localCodeWriter != null; localCodeWriter = localCodeWriter.next)
    {
      j++;
      i += localCodeWriter.getSize();
    }
    int k = 0;
    if (this.sourceFile != 0)
    {
      k++;
      i += 8;
    }
    if ((this.access & 0x20000) != 0)
    {
      k++;
      i += 6;
    }
    if ((this.access & 0x1000) != 0)
    {
      k++;
      i += 6;
    }
    if (this.innerClasses != null)
    {
      k++;
      i += 8 + this.innerClasses.length;
    }
    if (this.attrs != null)
    {
      k += this.attrs.getCount();
      i += this.attrs.getSize(this, null, 0, -1, -1);
    }
   
  private Item newFloat(float paramFloat)
  {
    this.key.set(paramFloat);
    Item localItem = get(this.key);
    if (localItem == null)
    {
      this.pool.putByte(4).putInt(Float.floatToIntBits(paramFloat));
      localItem = new Item(this.index++, this.key);
      put(localItem);
    }
    return localItem;
  }
  private Item newLong(long paramLong)
  {
    this.key.set(paramLong);
    Item localItem = get(this.key);
    if (localItem == null)
    {
      this.pool.putByte(5).putLong(paramLong);
      localItem = new Item(this.index, this.key);
      put(localItem);
      this.index = ((short)(this.index + 2));
    }
    return localItem;
  }
  private Item newDouble(double paramDouble)
  {
    this.key.set(paramDouble);
    Item localItem = get(this.key);
    if (localItem == null)
    {
      this.pool.putByte(6).putLong(Double.doubleToLongBits(paramDouble));
      localItem = new Item(this.index, this.key);
      put(localItem);
      this.index = ((short)(this.index + 2));
    }
    return localItem;
  }
  private Item newString(String paramString)
  {
    this.key2.set(8, paramString, null, null);
    Item localItem = get(this.key2);
    if (localItem == null)
    {
      this.pool.put12(8, newUTF8(paramString));
      localItem = new Item(this.index++, this.key2);
      put(localItem);
    }
    return localItem;
  }
  public int newNameType(String paramString1, String paramString2)
  {
    this.key2.set(12, paramString1, paramString2, null);
    Item localItem = get(this.key2);
    if (localItem == null)
    {
      put122(12, newUTF8(paramString1), newUTF8(paramString2));
      localItem = new Item(this.index++, this.key2);
      put(localItem);
    }
    return localItem.index;
  }
  private Item get(Item paramItem)
  {
    int i = paramItem.hashCode;
    for (Item localItem = this.items[(i % this.items.length)]; localItem != null; localItem = localItem.next)
      if ((localItem.hashCode == i) && (paramItem.isEqualTo(localItem)))
        return localItem;
    return null;
  }
}