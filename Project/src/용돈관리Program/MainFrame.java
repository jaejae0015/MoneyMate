package 용돈관리Program;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.text.SimpleDateFormat;
import java.sql.*;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.awt.BorderLayout;
import java.awt.EventQueue;
import javax.swing.DefaultComboBoxModel;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.SystemColor;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JTextField;
import javax.swing.JTabbedPane;
import java.awt.Color;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JTable;
import javax.swing.JCheckBox;
import javax.swing.JFormattedTextField;
import com.toedter.calendar.JDayChooser;
import com.toedter.calendar.JDateChooser;

public class MainFrame extends JFrame {

	
	
	private JPanel MainFrame;
	private JTextField totInput;
	private JTextField totOutput;
	private JTextField totTotal;
	private JTextField inputNameTxt;
	private JTable inputItemTb;
	private JTextField inputMoneyTxt;
	private JTable inputTable;
	private JTextField textField_5;
	private JTable table_2;
	private JTextField textField_6;
	private JTable table_3;
	private JTextField textField_8;
	private JTextField textField_9;
	private JTextField textField_10;
	private JTextField textField_11;
	private JTable table_4;
	private JTable table_5;
	private JTextField textField_12;
	private JTextField textField_13;
	private JTextField textField_14;
	private JTable table_6;
	private JTable table_7;
	private JTable table_8;
	private JTable table_9;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MainFrame frame = new MainFrame();
					frame.setVisible(true);
					
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
		//db연결부
		try {
					Class.forName("com.mysql.cj.jdbc.Driver");
					
					Connection con;//디비와 이어줄 connector변수 선언
					//connector와 연결//드라이버클래스://호스트주소/데이터베이스명,아이디,패스워드
					con = DriverManager.getConnection("jdbc:mysql://localhost/MyProgram?characterEncoding=UTF-8&serverTimezone=UTC","root", "3579");
					Statement st=con.createStatement();
					ResultSet rs;//결과값을 붑러온다
					String sql="CREATE TABLE IF NOT EXISTS 수입TB (InNumber INT(10) PRIMARY KEY , InItem CHAR(20) NOT NULL, InName CHAR(20) NOT NULL, InDate char(8) NOT NULL, InCome INT(30) NOT NULL)";
					st.executeUpdate(sql);
			
					//String sql="CREATE DATABASE MyProgram";
					//st.executeUpdate(sql);//SELECT제외는 다 이렇게 executeUpdate();
							
					//String sql="Create TABLE C(ENAME int)";
					//st.executeUpdate(sql);//SELECT제외는 다 이렇게 executeUpdate();
				
					
					//이거처럼 SELECT만 executeQuery();
//					rs = st.executeQuery("SHOW TABLES");
//		
//					if (st.execute("SHOW TABLES")) //execute는 RESULTSET을 리턴.
//					{
//						rs = st.getResultSet();//값을 가져온다.
//					}
//					while (rs.next()) {//NEXT()는 다음행으로 이동하는데, 끝까지 다 읽으면 false
//		
//						String str = rs.getNString(1);//그 행의 1열 값을 가져온다.
//						System.out.println(str);
//					}
		
				} 
		//에러 처리
		catch(ClassNotFoundException e)
		{
			System.out.println("드라이버가 존재하지 않습니다"+e);
		}
		catch (SQLException sqex) 
		{
		
					System.out.println("SQLException: " + sqex.getMessage());
					System.out.println("SQLState: " + sqex.getSQLState());
		
		}

	}

	/**
	 * Create the frame.
	 */
	public MainFrame() {
		setResizable(false);
	    
		
		setTitle("\uC6A9\uB3C8\uAD00\uB9AC\uD504\uB85C\uADF8\uB7A8");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 1261, 665);
		MainFrame = new JPanel();
		MainFrame.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(MainFrame);
		MainFrame.setLayout(null);
		
		setLocationRelativeTo(null);//화면 중앙배열.
		
		JPanel totPanel = new JPanel();
		totPanel.setLayout(null);
		totPanel.setBackground(SystemColor.activeCaption);
		totPanel.setBounds(0, 0, 1245, 57);
		MainFrame.add(totPanel);
		
		//맨위에 띄우는 tot부분
		JLabel label = new JLabel("\uCD1D\uC218\uC785");
		label.setFont(new Font("굴림체", Font.BOLD, 17));
		label.setBounds(40, 10, 51, 36);
		totPanel.add(label);
		
		totInput = new JTextField();
		totInput.setColumns(10);
		totInput.setBounds(103, 19, 116, 21);
		totPanel.add(totInput);
		
		JLabel label_1 = new JLabel("-");
		label_1.setFont(new Font("굴림체", Font.BOLD, 26));
		label_1.setBounds(231, 19, 20, 21);
		totPanel.add(label_1);
		
		JLabel label_2 = new JLabel("\uCD1D\uC9C0\uCD9C");
		label_2.setFont(new Font("굴림체", Font.BOLD, 17));
		label_2.setBounds(254, 10, 51, 36);
		totPanel.add(label_2);
		
		totOutput = new JTextField();
		totOutput.setColumns(10);
		totOutput.setBounds(317, 19, 116, 21);
		totPanel.add(totOutput);
		
		JLabel label_3 = new JLabel("=");
		label_3.setFont(new Font("굴림체", Font.BOLD, 26));
		label_3.setBounds(445, 19, 20, 21);
		totPanel.add(label_3);
		
		totTotal = new JTextField();
		totTotal.setColumns(10);
		totTotal.setBounds(477, 19, 116, 21);
		totPanel.add(totTotal);
		
		JTabbedPane tabbedPane = new JTabbedPane(JTabbedPane.TOP);
		tabbedPane.setBounds(0, 67, 1245, 569);
		MainFrame.add(tabbedPane);
		
		//수입부분
		JPanel inputPanel = new JPanel();
		tabbedPane.addTab("\uC218\uC785", null, inputPanel, null);
		inputPanel.setLayout(null);
		
		JPanel inputCaPanel = new JPanel();
		inputCaPanel.setLayout(null);
		inputCaPanel.setBackground(new Color(255, 228, 196));
		inputCaPanel.setBounds(12, 10, 344, 250);
		inputPanel.add(inputCaPanel);
		
		JLabel label_4 = new JLabel("\uCE74\uD14C\uACE0\uB9AC \uC124\uC815");
		label_4.setFont(new Font("굴림", Font.BOLD, 18));
		label_4.setBounds(12, 10, 121, 28);
		inputCaPanel.add(label_4);
		
		JButton inputCaBtn = new JButton("\uB4F1\uB85D");
		inputCaBtn.setFont(new Font("굴림", Font.BOLD, 15));
		inputCaBtn.setBackground(SystemColor.info);
		inputCaBtn.setBounds(268, 71, 64, 64);
		inputCaPanel.add(inputCaBtn);
		
		JLabel label_5 = new JLabel("\uB300\uD56D\uBAA9");
		label_5.setFont(new Font("굴림체", Font.BOLD, 17));
		label_5.setBounds(12, 56, 51, 36);
		inputCaPanel.add(label_5);
		
		JLabel label_6 = new JLabel("\uD56D\uBAA9\uBA85");
		label_6.setFont(new Font("굴림체", Font.BOLD, 17));
		label_6.setBounds(12, 99, 51, 36);
		inputCaPanel.add(label_6);
		
		String []inputItem= {"주수입","부수입"};
		JComboBox inputItemCmb = new JComboBox(inputItem);
		inputItemCmb.setBounds(75, 61, 181, 28);
		inputCaPanel.add(inputItemCmb);
		
		inputNameTxt = new JTextField();
		inputNameTxt.setColumns(10);
		inputNameTxt.setBounds(75, 102, 181, 33);
		inputCaPanel.add(inputNameTxt);
		
		inputItemTb = new JTable();
		inputItemTb.setBounds(12, 145, 320, 95);
		inputCaPanel.add(inputItemTb);
		
		JPanel inputMoPanel = new JPanel();
		inputMoPanel.setLayout(null);
		inputMoPanel.setBackground(new Color(255, 228, 196));
		inputMoPanel.setBounds(12, 261, 344, 250);
		inputPanel.add(inputMoPanel);
		
		JButton inputDataBtn2 = new JButton("\uC218\uC815");
		inputDataBtn2.setFont(new Font("굴림", Font.BOLD, 15));
		inputDataBtn2.setBackground(SystemColor.info);
		inputDataBtn2.setBounds(184, 205, 70, 35);
		inputMoPanel.add(inputDataBtn2);
		
		JButton inputDataBtn3 = new JButton("\uC0AD\uC81C");
		inputDataBtn3.setFont(new Font("굴림", Font.BOLD, 15));
		inputDataBtn3.setBackground(SystemColor.info);
		inputDataBtn3.setBounds(262, 205, 70, 35);
		inputMoPanel.add(inputDataBtn3);
		
		JLabel label_7 = new JLabel("\uB370\uC774\uD130 \uC785\uB825");
		label_7.setFont(new Font("굴림", Font.BOLD, 18));
		label_7.setBounds(12, 10, 121, 28);
		inputMoPanel.add(label_7);
		
		JLabel label_8 = new JLabel("\uD56D\uBAA9\uBA85");
		label_8.setFont(new Font("굴림체", Font.BOLD, 17));
		label_8.setBounds(36, 56, 51, 36);
		inputMoPanel.add(label_8);
		
		
		String []inputName= {"용돈","보너스","기타"};
		JComboBox inputNameCmb = new JComboBox(inputName);
		//inputNameCmb.addActionListener(new InNameAction());
		inputNameCmb.setBounds(99, 61, 181, 28);
		inputMoPanel.add(inputNameCmb);
		
		JLabel label_9 = new JLabel("\uAE08 \uC561");
		label_9.setFont(new Font("굴림체", Font.BOLD, 17));
		label_9.setBounds(36, 99, 51, 36);
		inputMoPanel.add(label_9);
		
		inputMoneyTxt = new JTextField();
		inputMoneyTxt.setColumns(10);
		inputMoneyTxt.setBounds(99, 102, 181, 33);
		inputMoPanel.add(inputMoneyTxt);
		
		JLabel label_10 = new JLabel("\uB0A0 \uC9DC");
		label_10.setFont(new Font("굴림체", Font.BOLD, 17));
		label_10.setBounds(36, 145, 51, 36);
		inputMoPanel.add(label_10);
		
		JDateChooser inputDateTxt = new JDateChooser();
		inputDateTxt.setBounds(99, 145, 181, 36);
		inputMoPanel.add(inputDateTxt);
		
		inputTable = new JTable();
		inputTable.setBounds(368, 10, 860, 501);
		inputPanel.add(inputTable);
		
		JPanel panel_3 = new JPanel();
		tabbedPane.addTab("\uC9C0\uCD9C", null, panel_3, null);
		panel_3.setLayout(null);
		
		JPanel panel_4 = new JPanel();
		panel_4.setLayout(null);
		panel_4.setBackground(new Color(255, 228, 196));
		panel_4.setBounds(12, 10, 344, 250);
		panel_3.add(panel_4);
		
		JLabel label_11 = new JLabel("\uCE74\uD14C\uACE0\uB9AC \uC124\uC815");
		label_11.setFont(new Font("굴림", Font.BOLD, 18));
		label_11.setBounds(12, 10, 121, 28);
		panel_4.add(label_11);
		
		JButton button_5 = new JButton("\uB4F1\uB85D");
		button_5.setFont(new Font("굴림", Font.BOLD, 15));
		button_5.setBackground(SystemColor.info);
		button_5.setBounds(268, 71, 64, 64);
		panel_4.add(button_5);
		
		JButton inputDataBtn1 = new JButton("\uB4F1\uB85D");
		inputDataBtn1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				 String a=inputNameCmb.getSelectedItem().toString();
				 String b=inputMoneyTxt.getText();
				 
				 
				 SimpleDateFormat fm = new SimpleDateFormat("yyyy-MM-dd");
				 String c=fm.format(inputDateTxt.getDate());
				 System.out.println(c);
				 
				 System.out.println(a);
				 System.out.println(b);
				 
			}
		});
		inputDataBtn1.setFont(new Font("굴림", Font.BOLD, 15));
		inputDataBtn1.setBackground(SystemColor.info);
		inputDataBtn1.setBounds(102, 205, 70, 35);
		inputMoPanel.add(inputDataBtn1);
		
		//지출 페이지
		JLabel label_12 = new JLabel("\uB300\uD56D\uBAA9");
		label_12.setFont(new Font("굴림체", Font.BOLD, 17));
		label_12.setBounds(12, 56, 51, 36);
		panel_4.add(label_12);
		
		JLabel label_13 = new JLabel("\uD56D\uBAA9\uBA85");
		label_13.setFont(new Font("굴림체", Font.BOLD, 17));
		label_13.setBounds(12, 99, 51, 36);
		panel_4.add(label_13);
		
		JComboBox comboBox_2 = new JComboBox();
		comboBox_2.setBounds(75, 61, 181, 28);
		panel_4.add(comboBox_2);
		
		textField_5 = new JTextField();
		textField_5.setColumns(10);
		textField_5.setBounds(75, 102, 181, 33);
		panel_4.add(textField_5);
		
		table_2 = new JTable();
		table_2.setBounds(12, 145, 320, 95);
		panel_4.add(table_2);
		
		JPanel panel_5 = new JPanel();
		panel_5.setLayout(null);
		panel_5.setBackground(new Color(255, 228, 196));
		panel_5.setBounds(12, 261, 344, 250);
		panel_3.add(panel_5);
		
		JButton button_6 = new JButton("\uB4F1\uB85D");
		button_6.setFont(new Font("굴림", Font.BOLD, 15));
		button_6.setBackground(SystemColor.info);
		button_6.setBounds(102, 205, 70, 35);
		panel_5.add(button_6);
		
		JButton button_7 = new JButton("\uC218\uC815");
		button_7.setFont(new Font("굴림", Font.BOLD, 15));
		button_7.setBackground(SystemColor.info);
		button_7.setBounds(184, 205, 70, 35);
		panel_5.add(button_7);
		
		JButton button_8 = new JButton("\uC0AD\uC81C");
		button_8.setFont(new Font("굴림", Font.BOLD, 15));
		button_8.setBackground(SystemColor.info);
		button_8.setBounds(262, 205, 70, 35);
		panel_5.add(button_8);
		
		JLabel label_14 = new JLabel("\uB370\uC774\uD130 \uC785\uB825");
		label_14.setFont(new Font("굴림", Font.BOLD, 18));
		label_14.setBounds(12, 10, 121, 28);
		panel_5.add(label_14);
		
		JLabel label_15 = new JLabel("\uD56D\uBAA9\uBA85");
		label_15.setFont(new Font("굴림체", Font.BOLD, 17));
		label_15.setBounds(36, 56, 51, 36);
		panel_5.add(label_15);
		
		JComboBox comboBox_3 = new JComboBox();
		comboBox_3.setBounds(99, 61, 181, 28);
		panel_5.add(comboBox_3);
		
		JLabel label_16 = new JLabel("\uAE08 \uC561");
		label_16.setFont(new Font("굴림체", Font.BOLD, 17));
		label_16.setBounds(36, 99, 51, 36);
		panel_5.add(label_16);
		
		textField_6 = new JTextField();
		textField_6.setColumns(10);
		textField_6.setBounds(99, 102, 181, 33);
		panel_5.add(textField_6);
		
		JLabel label_17 = new JLabel("\uB0A0 \uC9DC");
		label_17.setFont(new Font("굴림체", Font.BOLD, 17));
		label_17.setBounds(36, 145, 51, 36);
		panel_5.add(label_17);
		
		JDateChooser dateChooser_1 = new JDateChooser();
		dateChooser_1.setBounds(99, 145, 181, 36);
		panel_5.add(dateChooser_1);
		
		table_3 = new JTable();
		table_3.setBounds(368, 10, 860, 501);
		panel_3.add(table_3);
		
		JPanel panel_6 = new JPanel();
		tabbedPane.addTab("\uC608\uC0B0", null, panel_6, null);
		panel_6.setLayout(null);
		
		JPanel panel_7 = new JPanel();
		panel_7.setLayout(null);
		panel_7.setBackground(new Color(255, 228, 196));
		panel_7.setBounds(12, 10, 344, 250);
		panel_6.add(panel_7);
		
		JButton button_10 = new JButton("\uB4F1\uB85D");
		button_10.setFont(new Font("굴림", Font.BOLD, 15));
		button_10.setBounds(102, 205, 70, 35);
		panel_7.add(button_10);
		
		JButton button_11 = new JButton("\uC218\uC815");
		button_11.setFont(new Font("굴림", Font.BOLD, 15));
		button_11.setBounds(184, 205, 70, 35);
		panel_7.add(button_11);
		
		JButton button_12 = new JButton("\uC0AD\uC81C");
		button_12.setFont(new Font("굴림", Font.BOLD, 15));
		button_12.setBounds(262, 205, 70, 35);
		panel_7.add(button_12);
		
		JLabel label_18 = new JLabel("\uC608\uC0B0 \uC218\uC785 \uC785\uB825");
		label_18.setFont(new Font("굴림", Font.BOLD, 18));
		label_18.setBounds(12, 10, 135, 28);
		panel_7.add(label_18);
		
		JLabel label_19 = new JLabel("\uD56D\uBAA9\uBA85");
		label_19.setFont(new Font("굴림체", Font.BOLD, 17));
		label_19.setBounds(36, 56, 51, 36);
		panel_7.add(label_19);
		
		JComboBox comboBox_4 = new JComboBox();
		comboBox_4.setBounds(99, 61, 181, 28);
		panel_7.add(comboBox_4);
		
		JLabel label_20 = new JLabel("\uAE08 \uC561");
		label_20.setFont(new Font("굴림체", Font.BOLD, 17));
		label_20.setBounds(36, 99, 51, 36);
		panel_7.add(label_20);
		
		textField_8 = new JTextField();
		textField_8.setColumns(10);
		textField_8.setBounds(99, 102, 181, 33);
		panel_7.add(textField_8);
		
		textField_9 = new JTextField();
		textField_9.setColumns(10);
		textField_9.setBounds(99, 148, 181, 33);
		panel_7.add(textField_9);
		
		JLabel label_21 = new JLabel("\uB0A0 \uC9DC");
		label_21.setFont(new Font("굴림체", Font.BOLD, 17));
		label_21.setBounds(36, 145, 51, 36);
		panel_7.add(label_21);
		
		JButton button_13 = new JButton("\uC790\uB3D9\uB4F1\uB85D");
		button_13.setFont(new Font("굴림", Font.BOLD, 15));
		button_13.setBounds(215, 10, 117, 35);
		panel_7.add(button_13);
		
		JPanel panel_8 = new JPanel();
		panel_8.setLayout(null);
		panel_8.setBackground(new Color(255, 228, 196));
		panel_8.setBounds(12, 261, 344, 250);
		panel_6.add(panel_8);
		
		JButton button_14 = new JButton("\uB4F1\uB85D");
		button_14.setFont(new Font("굴림", Font.BOLD, 15));
		button_14.setBounds(102, 205, 70, 35);
		panel_8.add(button_14);
		
		JButton button_15 = new JButton("\uC218\uC815");
		button_15.setFont(new Font("굴림", Font.BOLD, 15));
		button_15.setBounds(184, 205, 70, 35);
		panel_8.add(button_15);
		
		JButton button_16 = new JButton("\uC0AD\uC81C");
		button_16.setFont(new Font("굴림", Font.BOLD, 15));
		button_16.setBounds(262, 205, 70, 35);
		panel_8.add(button_16);
		
		JLabel label_22 = new JLabel("\uC608\uC0B0 \uC9C0\uCD9C \uC785\uB825");
		label_22.setFont(new Font("굴림", Font.BOLD, 18));
		label_22.setBounds(12, 10, 135, 28);
		panel_8.add(label_22);
		
		JLabel label_23 = new JLabel("\uD56D\uBAA9\uBA85");
		label_23.setFont(new Font("굴림체", Font.BOLD, 17));
		label_23.setBounds(36, 56, 51, 36);
		panel_8.add(label_23);
		
		JComboBox comboBox_5 = new JComboBox();
		comboBox_5.setBounds(99, 61, 181, 28);
		panel_8.add(comboBox_5);
		
		JLabel label_24 = new JLabel("\uAE08 \uC561");
		label_24.setFont(new Font("굴림체", Font.BOLD, 17));
		label_24.setBounds(36, 99, 51, 36);
		panel_8.add(label_24);
		
		textField_10 = new JTextField();
		textField_10.setColumns(10);
		textField_10.setBounds(99, 102, 181, 33);
		panel_8.add(textField_10);
		
		textField_11 = new JTextField();
		textField_11.setColumns(10);
		textField_11.setBounds(99, 148, 181, 33);
		panel_8.add(textField_11);
		
		JLabel label_25 = new JLabel("\uB0A0 \uC9DC");
		label_25.setFont(new Font("굴림체", Font.BOLD, 17));
		label_25.setBounds(36, 145, 51, 36);
		panel_8.add(label_25);
		
		JButton button_17 = new JButton("\uC790\uB3D9\uB4F1\uB85D");
		button_17.setFont(new Font("굴림", Font.BOLD, 15));
		button_17.setBounds(215, 10, 117, 35);
		panel_8.add(button_17);
		
		table_4 = new JTable();
		table_4.setBounds(385, 10, 394, 394);
		panel_6.add(table_4);
		
		table_5 = new JTable();
		table_5.setBounds(822, 10, 394, 394);
		panel_6.add(table_5);
		
		JLabel label_26 = new JLabel("\uC608\uC0B0 \uC218\uC785 \uAE08\uC561:");
		label_26.setFont(new Font("굴림체", Font.BOLD, 17));
		label_26.setBounds(425, 414, 132, 36);
		panel_6.add(label_26);
		
		textField_12 = new JTextField();
		textField_12.setColumns(10);
		textField_12.setBounds(556, 417, 181, 33);
		panel_6.add(textField_12);
		
		JLabel label_27 = new JLabel("-");
		label_27.setFont(new Font("굴림체", Font.BOLD, 26));
		label_27.setBounds(800, 426, 20, 21);
		panel_6.add(label_27);
		
		JLabel label_28 = new JLabel("\uC608\uC0B0 \uC9C0\uCD9C \uAE08\uC561:");
		label_28.setFont(new Font("굴림체", Font.BOLD, 17));
		label_28.setBounds(865, 417, 132, 36);
		panel_6.add(label_28);
		
		textField_13 = new JTextField();
		textField_13.setColumns(10);
		textField_13.setBounds(996, 420, 181, 33);
		panel_6.add(textField_13);
		
		JLabel label_29 = new JLabel("\uCD1D \uAE08\uC561");
		label_29.setFont(new Font("굴림체", Font.BOLD, 17));
		label_29.setBounds(671, 475, 72, 36);
		panel_6.add(label_29);
		
		textField_14 = new JTextField();
		textField_14.setColumns(10);
		textField_14.setBounds(755, 478, 181, 33);
		panel_6.add(textField_14);
		
		JPanel panel_9 = new JPanel();
		tabbedPane.addTab("\uAC80\uC0C9", null, panel_9, null);
		panel_9.setLayout(null);
		
		JCheckBox checkBox = new JCheckBox("\uAE30\uAC04\uAC80\uC0C9");
		checkBox.setFont(new Font("굴림", Font.BOLD, 16));
		checkBox.setBounds(78, 10, 99, 32);
		panel_9.add(checkBox);
		
		JCheckBox checkBox_1 = new JCheckBox("\uD56D\uBAA9\uAC80\uC0C9");
		checkBox_1.setFont(new Font("굴림", Font.BOLD, 16));
		checkBox_1.setBounds(181, 10, 99, 32);
		panel_9.add(checkBox_1);
		
		JComboBox comboBox_6 = new JComboBox();
		comboBox_6.setBounds(307, 10, 238, 32);
		panel_9.add(comboBox_6);
		
		JFormattedTextField formattedTextField = new JFormattedTextField();
		formattedTextField.setBounds(568, 11, 515, 32);
		panel_9.add(formattedTextField);
		
		JButton button_18 = new JButton("\uAC80\uC0C9");
		button_18.setFont(new Font("굴림", Font.BOLD, 16));
		button_18.setBounds(1092, 10, 80, 32);
		panel_9.add(button_18);
		
		table_6 = new JTable();
		table_6.setBounds(45, 59, 1148, 452);
		panel_9.add(table_6);
		
		JPanel panel_10 = new JPanel();
		tabbedPane.addTab("\uD1B5\uACC4", null, panel_10, null);
		panel_10.setLayout(null);
		
		JTabbedPane tabbedPane_1 = new JTabbedPane(JTabbedPane.TOP);
		tabbedPane_1.setBounds(12, 10, 1216, 520);
		panel_10.add(tabbedPane_1);
		
		JPanel panel_11 = new JPanel();
		tabbedPane_1.addTab("\uAE30\uBCF8\uD1B5\uACC4", null, panel_11, null);
		panel_11.setLayout(null);
		
		JPanel panel_12 = new JPanel();
		tabbedPane_1.addTab("\uC608\uC0B0\uD1B5\uACC4", null, panel_12, null);
		panel_12.setLayout(null);
		
		table_7 = new JTable();
		table_7.setBounds(22, 10, 702, 462);
		panel_12.add(table_7);
		
		JLabel label_30 = new JLabel("\uC218\uC785\uC21C\uC704");
		label_30.setFont(new Font("굴림체", Font.BOLD, 17));
		label_30.setBounds(758, 10, 74, 36);
		panel_12.add(label_30);
		
		table_8 = new JTable();
		table_8.setBounds(758, 42, 422, 190);
		panel_12.add(table_8);
		
		JLabel label_31 = new JLabel("\uC9C0\uCD9C\uC21C\uC704");
		label_31.setFont(new Font("굴림체", Font.BOLD, 17));
		label_31.setBounds(758, 250, 74, 36);
		panel_12.add(label_31);
		
		table_9 = new JTable();
		table_9.setBounds(758, 282, 422, 190);
		panel_12.add(table_9);
	}
}
