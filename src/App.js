import React, { Component } from 'react'
import './App.css'
import MatchHistory from './MatchHistory'
import Header from './Header.js'
import Heroes from './Heroes'
import About from './About'
import Pro from './Pro'
import GameStats from './GameStats'
import Footer from './Footer'
import Login from './Login.jsx'
import { Switch, Route } from 'react-router-dom'
import { withRouter } from 'react-router'
import HeroStats from './HeroStats'
import Items from './Items'
import ItemStats from './ItemStats'
import Tips from './Tips'

class App extends Component {
  constructor (props) {
    super(props)
    this.state = {
      activeKey: 1,
      players: {
        personaname: '',
        mmr_estimate: '',
        rank_tier: '',
        solo_competitive_rank: '',
        avatar: ''
      },
      wl: { win: '', lose: '' },
      recentMatches: [],
      heroes: [],
      currentID: undefined,
      heroid: 1
    }
  }

  onLogin = () => {
    this.setState({
      isLoggedIn: true
    })
  }

  onLogout = () => {
    this.setState(
      { isLoggedIn: undefined }, () => {
        this.state.history.push('/')
      }
    )
  }  

  onChangeSearchText = (event) => {
    this.setState({ text: event.target.value })
  }


  handleSelect(selectedKey) {
    this.setState({ activeKey: selectedKey });
  } 

  getGenericID = () => {
    this.setState({ text: '' })
  }


  render () {
    const { isLoggedIn, account_id , heroid, matchid ,itemid} = this.state
    return (
      <div className='App'>
        <Header
          isLoggedIn={isLoggedIn}
          onLogin={this.onLogin}
          onLogout={this.onLogout}
          hero_id={this.hero_id}          
          onChangeSearchText={this.onChangeSearchText}
          text={this.state.text}
          handleSelect={this.handleSelect}
          activeKey={this.state.activeKey}
        />

        <Switch>
          <Route exact path='/'  render={props => (
              <Login {...props}
                getGenericID={this.getGenericID}
              />
            )}/>
          <Route
            path='/match/:id'
            render={props => (
              <MatchHistory
                {...props}
                isLoggedIn={isLoggedIn}
                account_id={account_id}
                heroid = {heroid}
                matchid = {matchid}
                itemid = {itemid}
                players={this.state.players}
                wl={this.state.wl}
                recentMatches={this.state.recentMatches}
                skill={this.state.skill}
                heroes={this.state.heroes}
              />
            )}
          />
          <Route
            exact path='/heroes'
            render={props => (
              <Heroes {...props} account_id={this.state.text} />
            )}
          />  
          <Route
            exact path='/items'
            render={props => (
              <Items {...props}/>
            )}
          />  

         <Route
            exact path='/pro'
            render={props => (<Pro {...props} account_id={this.state.text}  />) }
          />  
          <Route exact path='/about' render={props => (<About />)} />          
          <Route exact path='/heroes/:heroid' component={HeroStats}  render={props => (<HeroStats {...props} heroid={heroid}  />)}  />
          <Route exact path='/games/:matchid' component={GameStats}  render={props => (<GameStats {...props} matchid={matchid}  />)}  />
          <Route exact path='/items/:itemid' component={ItemStats}  render={props => (<ItemStats {...props} itemid={itemid}  />)}  />
          <Route exact path='/Tips' render={props => (<Tips />)} />          
 

        </Switch>
            <br/>

                     <Footer/>

      </div>

    )
  }
}

export default withRouter(App)
