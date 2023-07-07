const sections=document.querySelectorAll(".section");
const section_buttons=document.querySelectorAll(".controls");
const section_button=document.querySelectorAll(".control");
const allSections = document.querySelector(".main-content");

function PageTransitions(){
    // Button click active class
    for(let i=0; i< section_button.length; i++){
        section_button[i].addEventListener("click", function(){
            let current_button=document.querySelectorAll(".active-btn");
            current_button[0].classList.remove("active-btn");
            section_button[i].classList.add("active-btn");
        })
    }

    // Active Sections
    allSections.addEventListener("click", (e)=>{
        const id= e.target.dataset.id;

        if(id){
            // Remove Selected from the other buttons
            section_button.forEach((button) => {
                button.classList.remove("active-btn")
            })
            e.target.classList.add("active-btn")

            // hide other sections
            sections.forEach((section)=>{
                section.classList.remove("active")
            })

            const element=document.getElementById(id);
            element.classList.add("active");
        }
    })
    
}

PageTransitions();

function downloadResume(){
    window.open("https://drive.google.com/uc?export=download&id=16vWR-UfNe0y_Ar-E-zhv_JcRNNdqUdKv", "_blank");
}

function openLinkedin(){
    window.open("https://www.linkedin.com/in/ramankumar-1/", target="_blank")
}
function openGithub(){
    window.open("https://github.com/ramankumar-1", target="_blank")
}
function openKaggle(){
    window.open("https://www.kaggle.com/theramankumar", target="_blank")
}

function openGmail(){
    window.open("mailto:ramankumar4141410@gmail.com", target="_blank")
}

function toggleMode(){
    // document.body.classList.toggle("darkmode");
    var element = document.body;
    var nightModeButton=document.getElementById("nightModebutton");

    if (element.className==="main-content dark-mode"){
        nightModeButton.innerHTML='<i class="fa-solid fa-sun fa-2xl"></i>';
    }
    else{
        nightModeButton.innerHTML='<i class="fa-solid fa-moon fa-2xl" style="color: #ffffff;"></i>';
    }
   element.classList.toggle("dark-mode");
}
