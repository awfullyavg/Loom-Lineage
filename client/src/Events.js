import React from "react";
import { useState, useEffect } from "react";

function Events () {
    const [events, setEvents] = useState([])
    const [eventName, setEventName] = useState('')
    const [eventDescription, setEventDescription] = useState('')

    useEffect(() => {
        fetch('/events')
        .then(resp => resp.json())
        .then(events => setEvents(events))
    }, [])

    function handleEventSubmit () {
        const new_event = {
            name: eventName,
            description: eventDescription
        }

        fetch('/events', {
            method: 'POST',
            headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            },
            body : JSON.stringify(new_event)
        })
        .then(resp => resp.json())
        .then(new_event => setEvents([...events, new_event]))

        setEventDescription('')
        setEventName('')

    }



    return (
        <div>
            <div>
                <p>{eventName}</p>
                <p>{eventDescription}</p>
            </div>
            <h1>Make an Event for your Family!</h1>
            <form onSubmit={handleEventSubmit}>
                <label>Title of your Event</label><br></br>
                <input type="text" onChange={(e) => setEventName(e.target.value)} value={eventName}/> <br></br>
                <label>Description</label><br></br>
                <textarea placeholder="Dont forget to put the date & time!" onChange={(e) => setEventDescription(e.target.value)} value={eventDescription} />
                <button>Add Event</button>
            </form>
        </div>

    )
}

export default Events