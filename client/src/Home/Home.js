import React from "react";


function Home() {
    
    
    return(
        <div className="home">
            <header class=" text-black p-6">
                <div class="container mx-auto text-center">
                    <h1 class="text-3xl font-semibold">Loom Lineage</h1>
                    <p class="mt-2 text-lg">Never lose track of what matters the most!</p>
                </div>
            </header>
            <div class="container mx-auto mt-8 px-4">
    <div class="flex flex-col-reverse md:flex-row items-center">

        <div class="md:w-1/2 pb-10">
            <img src="https://img.freepik.com/free-photo/happy-black-parents-with-kids-making-video-call-smart-phone-home_637285-11501.jpg?w=1380&t=st=1691601201~exp=1691601801~hmac=5b7c036c9dd1119142504bdc60d531bce7e1f6413582c1b0fbbe6074d28256b4" alt="App Screenshot" class="w-full rounded-lg shadow-md" />
        </div>


        <div class="md:w-1/2 md:ml-8">
            <h2 class="text-2xl font-semibold mb-4">Your Family Lineage, All In One place</h2>
            <p class="text-gray-700 mb-4">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            <button class=" bg-Chinese-Violet hover:bg-violet-400 text-white px-4 py-2 rounded-md">Get Started</button>
        </div>
    </div>
</div>

        </div>
        
    )
}

export default Home


