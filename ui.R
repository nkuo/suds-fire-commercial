# Data dashboard for Metro21 Fire Project
# Author: Qianyi Hu
# Date: May 27, 2017

getwd()
setwd("/home/nathan/Documents/Student_Data/dev/2017_suds-fire")
# This is the ui part of the dashboard

library(shiny)
library(markdown)

shinyUI(fluidPage(
  # sidebar
  
  sidebarLayout(
    
    
    sidebarPanel(
      # select x-axis in the visualization plot
      
      selectInput("yvar","Display",
                  choices = c("Fire Incidents","Fire Risk", "Fire Inspections"),
                  selected = "Fire Incidents",
                  multiple = FALSE),
      selectInput("xvar",label=NULL,
                    choices = c("Property Classification","Property Usage Type","Neighborhood","Fire District"),
                    selected = "State",
                    multiple = FALSE),

      # by default, it is set to include all fire codes
       checkboxGroupInput("checkGroup",
                         label = "Select fire codes",
                         choices = list("All 100s"=1,
                                        "All 200s"=2,
                                        "All 300s"=3,
                                        "All 400s"=4,
                                        "All 500s"=5,
                                        "All 600s"=6,
                                        "All 700s"=7
                                        ),
                         inline=TRUE
                         ),
      selectInput("code",
                  label = NULL,
                  choices = c("All Fire Incident Types", as.vector(sort(unique(fire_model$full.code)))),
                  selected = "All Fire Incident Types",
                  multiple = TRUE),
      dateRangeInput("dates",label = "Select date range",start = "2009-01-01", end = NULL,format = "yyyy-mm-dd"),

      
      
      selectInput("property",
                  label = "Select Property type",
                  choices = c("All Classification Types",as.vector(sort(unique(model$STATEDESC)))),
                  selected = "All Classification Types",
                  multiple=TRUE),
      selectInput("use",
                  label = NULL,
                  choices = c("All Usage Types",as.vector(sort(unique(model$USEDESC)))),
                  selected = "All Usage Types",
                  multiple=TRUE),
      selectInput("nbhood",
                  label = "Select location",
                  choices = c("All Neighborhoods", as.vector(sort(unique(model$hood_x)))),
                  selected = "All Neighborhoods",
                  multiple=TRUE),
      selectInput("fire_dst",
                  label = NULL,
                  choices = c("All Fire Districts",as.vector(sort(unique(model$Pgh_FireDistrict_x)))),
                  selected = "All Fire Districts",
                  multiple=TRUE),
      sliderInput("range",
                  label="Risk range:",
                  min=1, max=10, value=c(1, 10)),
      
      
    width=3),
    mainPanel(
      # divided into 3 tab panels, visualization, table, inspection
      tabsetPanel(
        
        # visualization tab includes the bar chart with selected options
        tabPanel("Visualization",
                 wellPanel(
                   div(style="display: inline-block;vertical-align:top", p("Number of records selected:")),
                   div(style="display: inline-block;vertical-align:top;text-align:center", textOutput("n_records")),
                   div(style="display: inline-block;vertical-align:top;float:right", downloadButton("plotVis",label = "Download"))
                 ),
                 div(style="display: inline-block;vertical-align:top;float:right", plotOutput("distPlot"))
                 ),
        # the table tab includes the table with selected options (another format of the visualization with the same filtered data)
        # it also has the download option to download the table as a csv file.
        tabPanel("Table", 
                 downloadButton('downloadTable', label='Download'),
                 dataTableOutput("table")
                 )
        
        # the inspection plot is static, showing the inspection counts and also the percentage of inspected address by property type.
       
      )
    )
  ))
)
