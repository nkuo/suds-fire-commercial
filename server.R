# Data dashboard for Metro21 Fire Project
# Author: Qianyi Hu
# Date: May 27, 2017


# The server side of the dashboard
#install.packages("plotly")
library(shiny)
library(ggplot2)
library(dplyr)
library(plotly)

getwd()
setwd("/Users/mmadaio/R Projects/Metro21")



shinyServer(function(input, output) {
  
  # read data
  fire_model <- read.csv("data/pcafire.csv") 
  colnames(fire_model) <- c("X", "House_Num", "Street_Name", "Address", "STATEDESC","School_District","Owner","Municipalities","Neigh.Code",
                       "TaxDesc","USEDESC","Lot_Area","Sales_Price", "FairMarketLand", "FairMarketBuilding","Inspection_Date",
                       "Inspection_Result", "Violation", "Violation_Year", "Street_Num", "Street", "Call_Created_Date", "Fire_Code",
                       "Response_Time", "Fire_Year","Fire", "hood_x", "Incident_Type")
  
  
  model <- read.csv("data/pitt_risk_inspection_merged.csv")
  
  inspect0 <- read.csv("data/Fire_Inspection_percentage_0605.csv")
  
  # pre-process
#  print(fire_model$Call_Created_Date)
  time <- as.Date(fire_model$Call_Created_Date,"%m/%d/%Y")
  year <- as.factor(as.numeric(format(time,"%Y")))
  month <- as.factor(as.numeric(format(time,"%m")))


  fire_model$TIME <- time
  fire_model$Year <- year
  fire_model$Month <- month

  model$Score <- model$RiskScore


  # get data subset
  data <- reactive({
    # default option: select all
   if (input$yvar == "Fire Incidents") {
       print("Filtering Fire Incidents")

         # filter by fire codes
         all_code <- levels(fire_model$Fire_Code)
         codes <- c()
         selectGroup <- as.vector(input$checkGroup)
         
         if (1 %in% selectGroup){
           codes <- c(codes, all_code[substr(all_code,1,1)=="1"])
         }
         if (2 %in% selectGroup){
           codes <- c(codes, all_code[substr(all_code,1,1)=="2"])
         }
         if (3 %in% selectGroup){
           codes <- c(codes, all_code[substr(all_code,1,1)=="3"])
         }
         if (4 %in% selectGroup){
           codes <- c(codes, all_code[substr(all_code,1,1)=="4"])
         }
         if (5 %in% selectGroup){
           codes <- c(codes, all_code[substr(all_code,1,1)=="5"])
         }
         if (6 %in% selectGroup){
           codes <- c(codes, all_code[substr(all_code,1,1)=="6"])
         }
         if (7 %in% selectGroup){
           codes <- c(codes, all_code[substr(all_code,1,1)=="7"])
         }
         # & TIME<=input$dates[2] & TIME >= input$dates[1]
          
         d <- subset(fire_model, subset = (Fire_Code %in% c(codes, input$code)))
             
         if (("All Fire Incident Types" %in% input$code)) {
           d <-  subset(fire_model) #, subset = TIME<=input$dates[2] & TIME >= input$dates[1])
         }
         
         
         # filter by property type (STATEDESC)
         if (!("All Classification Types" %in% input$property)){
           d <- subset(d, subset=(STATEDESC %in% input$property))
         }
         
         # filter by usage type (USEDESC)
         if (!("All Usage Types" %in% input$use)) {
           d <- subset(d, subset=(USEDESC %in% input$use))
         }
         
         # filter by neighborhood (NEIGHDESC)
         if (!("All Neighborhoods" %in% input$nbhood)) {
           d <- subset(d, subset=(hood_x %in% input$nbhood))
         }
         # filter by fire district
         if (!("All Fire Districts" %in% input$fire_dst)){
           d <- subset(d, subset=(Pgh_FireDistrict_x %in% input$fire_dst)) 
         }
        
         d
         
   
    } else {
       print("Filtering Fire Risk")
       
      # if (input$all == TRUE){
      #     d <- subset(model, subset = (Score <= input$range[2] & Score >= input$range[1]))
      #     print(d)
      # }
      
      d <- subset(model, subset = (Score <= input$range[2] & Score >= input$range[1]))
     # print(d)
      
      # filter by property type (STATEDESC)
      if (!("All Classification Types" %in% input$property)){
        d <- subset(d, subset=(STATEDESC %in% input$property))
      }
      
      # filter by usage type (USEDESC)
      if (!("All Usage Types" %in% input$use)) {
        d <- subset(d, subset=(USEDESC %in% input$use))
      }
      
      # filter by neighborhood (NEIGHDESC)
      if (!("All Neighborhoods" %in% input$nbhood)) {
        d <- subset(d, subset=(hood_x %in% input$nbhood))
      }
      # filter by fire district
      if (!("All Fire Districts" %in% input$fire_dst)){
        d <- subset(d, subset=(hood_x %in% input$fire_dst)) 
      }
      d
    }
     
    
    
   # print(d)
  })
  
  # Visualization output plot
  plot_Vis <- reactive({
    
      if (input$xvar == "Property Classification") {
        x_axis <- "STATEDESC"
      } else if (input$xvar == "Property Usage Type") {
        x_axis <- "USEDESC"
      } else if (input$xvar == "Neighborhood") {
        x_axis <- "hood_x"
      }
      
      if (input$yvar == "Fire Risk") {
        if (input$xvar == "Fire District") {
        x_axis <- "Pgh_FireDistrict_x"
      } 
     
    } else if (input$yvar == "Fire Incidents") {
      
      
      if (input$xvar == "Fire District") {
        x_axis <- "hood_x"
      }
    }
    
    y_axis <- input$yvar
    #print(y_axis)
   
    
    
    
    # Two types of y axis: number of records and risk score
    if (y_axis == "Fire Incidents"){
      print("displaying Fires")
      
      data_selected <- data()[!is.na(data()[[x_axis]]),]
      ag_data <- as.data.frame(table(data_selected[x_axis]))
      data_order <- as.vector(unlist(ag_data[order(ag_data[2]),][1]))
      
      
      # Here if the number of bars is over 15, it will be better to rotate the axis and make it horizontal bar charts 
      # (especially for usage types and neighborhood types)
      if (nlevels(data()[[x_axis]]) <= 15){
        plot <- ggplot(data = data()[!is.na(data()[[x_axis]]),],aes(x=data()[!is.na(data()[[x_axis]]),][[x_axis]])) + 
          geom_bar(width=0.2,stat = "count",fill="cadetblue") + 
          theme(plot.title = element_text(size = 15, face = "bold"),text = element_text(size=15)) +
          geom_text(stat="count",aes(label=..count..),vjust=-1,cex=5) +
          ggtitle(paste("Fire Incidents by",x_axis)) +
          scale_x_discrete(limits=data_order,labels=data_order) +
          
          xlab(x_axis) +
          ylab("Number of Records")
        
      }else{
        
        
        plot <- ggplot(data = data()[!is.na(data()[[x_axis]]),],aes(x=data()[!is.na(data()[[x_axis]]),][[x_axis]])) + 
          geom_bar(stat = "count",width=0.8,fill="cadetblue") + 
          theme(plot.title = element_text(size = 18, face = "bold"),text = element_text(size=14)) +
          geom_text(stat="count",aes(label=..count..),geom = "text",size=3,hjust =-0.5,cex=2) +
          
          ggtitle(paste("Fire Incidents by",x_axis)) +
          scale_x_discrete(limits=data_order,labels=data_order) +
          coord_flip() + 
          xlab(x_axis) +
          ylab("Number of Records")
        
      }
      
    }else if (y_axis == "Fire Risk"){
      print("displaying Fire risk")
      
     
      # consider average risk score by x axis
      if (nlevels(data()[[x_axis]]) <= 15){
        plot <- ggplot(data = data()[!is.na(data()[[x_axis]]),],aes(x=data()[!is.na(data()[[x_axis]]),][[x_axis]],y=Score)) + 
          stat_summary(fun.y = "mean",geom = "bar",width=0.8,fill="steelblue") + 
          stat_summary(aes(label=..y..),fun.y = function(x){round(mean(x),2)},geom = "text",size=5,vjust=-1,width=0.8) +
          theme(plot.title = element_text(size = 18, face = "bold"),text = element_text(size=15)) +
          ggtitle("Average Risk Score") + ylim(0,10) + 
          xlab(x_axis) +
          ylab("Risk Score")
        
      }else{
        data_selected <- data()[!is.na(data()[[x_axis]]),]
        
        ag_score <- aggregate(data_selected[["Score"]] ~ data_selected[[x_axis]], data_selected, mean)
        ag_label <- as.vector(unlist(ag_score[order(ag_score[2]),][1]))
        print(length(ag_label))
        # h = 550 + 10 * length(ag_label)
        plot <- ggplot(data = data_selected, aes(x=data_selected[[x_axis]],y=Score)) + 
          stat_summary(fun.y = "mean",geom = "bar",width=0.8,fill="steelblue") + 
          coord_flip() + scale_x_discrete(limits=ag_label,labels=ag_label) +
          stat_summary(aes(label=..y..),fun.y = function(x){round(mean(x),2)},geom = "text",size=4,hjust=-1) +
          ggtitle("Average Risk Score") + ylim(0,10) + 
          theme(plot.title = element_text(size = 18, face = "bold"),text = element_text(size=14)) +
          xlab(x_axis) +
          ylab("Risk Score")
      }
      
    } else if (y_axis == "Fire Inspections") {
        inspect <- inspect0[inspect0$INSPECTED!=0,] #subset(inspect0[order(inspect0[,2]),],subset = inspect$INSPECTED!=0)
        lab <- paste(round(inspect$INSPECTED / inspect$TOTAL.ADDRESSES * 100,2),"%",sep="")
        plot <- ggplot(data=inspect, aes(x=USEDESC,y=INSPECTED))+ geom_bar(stat = "identity",position="dodge",fill="darkcyan") + coord_flip() + 
          ggtitle("Inspection Counts and Percentage by Usage Type") + 
          theme(plot.title = element_text(size = 22, face = "bold"),text = element_text(size=16))+
          xlab("Usage Description")+ylab("Total & Percent Inspected Addresses of Each Type")+
          scale_x_discrete(limits=inspect$USEDESC) +
          geom_text(label=lab,cex=5,hjust=0)
    }
    plot
  })

  

    
  
  myHeight <- function(){
    
    
    #print(data_selected)
    
    if (input$yvar == "Fire Risk") {
      
        if (input$xvar == "Property Classification") {
          x_axis <- "STATEDESC"
        } else if (input$xvar == "Property Usage Type") {
          x_axis <- "USEDESC"
        } else if (input$xvar == "Neighborhood") {
          x_axis <- "hood_x"
        } else if (input$xvar == "Fire District") {
          x_axis <- "Pgh_FireDistrict_x"
        } 
        data_selected <- data()[!is.na(data()[[x_axis]]),]
      
        ag_score <- aggregate(data_selected[["Score"]] ~ data_selected[[x_axis]], data_selected, mean)
        ag_label <- as.vector(unlist(ag_score[order(ag_score[2]),][1]))
    
    } else if (input$yvar == "Fire Incidents") {
      
      
      if (input$xvar == "Property Classification") {
        x_axis <- "STATEDESC"
      } else if (input$xvar == "Property Usage Type") {
        x_axis <- "USEDESC"
      } else if (input$xvar == "Neighborhood") {
        x_axis <- "hood_x"
      } else if (input$xvar == "Fire District") {
        x_axis <- "hood_x"
      }
        print("x axis is:")
        print(x_axis)
        data_selected <- data()[!is.na(data()[[x_axis]]),]

        ag_data <- aggregate(data_selected[["X"]] ~ data_selected[[x_axis]], data_selected, length)
        ag_label <- as.vector(unlist(ag_data[order(ag_data[2]),][1]))
    }
    
    num = length(ag_label)
    print(num)
    
    if (num < 20) {
      modifier = 3
    } else {
      modifier = 200
    }
    print(modifier)
    return(650 + 5 * modifier)
  }
  
  # visualization plot
  output$distPlot <- renderPlot({
    
    plot_Vis()
  }, 
  
  width=850,height=myHeight)

  
  
  # download plotVis
  output$plotVis <- downloadHandler(
    
    filename <- "visualization.png",
    content <- function(file){
      dpi_val <- 85
      h <- (myHeight()/dpi_val)
      print(myHeight())
      print(h)
      ggsave(file, plot = plot_Vis(),device = "png",width=11, height=h,units="in",dpi=dpi_val)
    }
  )
  
  # inspection table
  output$table <- renderDataTable({
    res <- as.data.frame(data())[c(1:3,86,13,15,17,23,25,99,129)] # only display selected columns
    res
    })
  
  # download table
  output$downloadTable <- downloadHandler(
    filename = "table.csv",
    content = function(file) {
      write.csv(as.data.frame(data())[c(1:3,86,13,15,17,23,25,99,129)], file)
    }
  )
  
  # print total number of records selected (for reference)
  output$n_records <- renderText({
    nrow(data())
  })

  
  # reactive plot
  plot_Inspection <- reactive({
    inspect <- inspect0[inspect0$INSPECTED!=0,] #subset(inspect0[order(inspect0[,2]),],subset = inspect$INSPECTED!=0)
    lab <- paste(round(inspect$INSPECTED / inspect$TOTAL.ADDRESSES * 100,2),"%",sep="")
    p <- ggplot(data=inspect, aes(x=USEDESC,y=INSPECTED))+ geom_bar(stat = "identity",position="dodge",fill="darkcyan") + coord_flip() + 
      ggtitle("Inspection Counts and Percentage by Usage Type") + 
      theme(plot.title = element_text(size = 22, face = "bold"),text = element_text(size=16))+
      xlab("Usage Description")+ylab("Total & Percent Inspected Addresses of Each Type")+
      scale_x_discrete(limits=inspect$USEDESC) +
      geom_text(label=lab,cex=5,hjust=0)
    p
  })
  
  # plot inspection
  output$plotInspect <- renderPlot({
    p <- plot_Inspection()
    p
  },height=600,width=800)
  
  #download inspection plot
  output$downloadPlotInspect <- downloadHandler(
    filename <- "Inspection.png",
    content <- function(file){
      ggsave(file, plot = plot_Inspection(),device = "png",width = 15, height = 12,units = "in")
    }
  )

})
